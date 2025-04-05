import pickle
import os
import numpy as np
from scapy.layers.inet import IP, TCP, UDP, ICMP
from ids_core.notifications.email_notifier import send_email_notification

# Load the pre-trained model
def load_model():
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'NSL-KDD/model.pkl')
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Extract features from packet
def extract_features(packet):
    features = []
    
    # Basic IP features
    if IP in packet:
        features.append(len(packet))  # Packet length
        features.append(packet[IP].ttl)  # Time to live
        features.append(packet[IP].proto)  # Protocol
        
        # TCP features
        if TCP in packet:
            features.append(packet[TCP].sport)  # Source port
            features.append(packet[TCP].dport)  # Destination port
            features.append(int(packet[TCP].flags.A))  # ACK flag
            features.append(int(packet[TCP].flags.S))  # SYN flag
            features.append(int(packet[TCP].flags.F))  # FIN flag
            features.append(int(packet[TCP].flags.R))  # RST flag
            features.append(int(packet[TCP].flags.P))  # PSH flag
        else:
            # Padding with zeros if no TCP
            features.extend([0, 0, 0, 0, 0, 0, 0])
            
        # Additional features like payload size
        features.append(len(packet.payload))
    else:
        # If no IP layer, pad with zeros
        features.extend([0] * 12)
        
    return np.array(features).reshape(1, -1)  # Reshape for sklearn model input

def analyze_packet(packet, logger=None):
    # Load the model if not already loaded
    model = load_model()
    if model is None:
        if logger:
            logger.error("Failed to load model for packet analysis")
        return False
    
    try:
        # Extract features from the packet
        features = extract_features(packet)
        
        # Make prediction
        prediction = model.predict(features)
        
        # Determine if malicious (assuming 1 means malicious)
        is_malicious = prediction[0] == 1
        
        if logger:
            if is_malicious:
                logger.warning(f"MALICIOUS PACKET DETECTED: {packet.summary()}")
            else:
                logger.debug(f"Benign packet: {packet.summary()}")
        
        if is_malicious:
            notify_user(packet)
            
        return is_malicious
    except Exception as e:
        if logger:
            logger.error(f"Error analyzing packet: {e}")
        return False

def notify_user(packet):
    recipient_email = "bhatthariohm2004@gmail.com"  # Replace with actual recipient email
    subject = "Malicious Packet Detected"
    message = f"A malicious packet was detected:\n\n{packet.summary()}\n\nFull packet details:\n{packet.show(dump=True)}"
    
    # Using the correct function name as per your email_notifier.py
    send_email_notification(recipient_email, subject, message)