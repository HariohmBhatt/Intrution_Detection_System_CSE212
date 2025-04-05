import logging
import os
from datetime import datetime
from scapy.all import sniff

def setup_logger(name="ids_core", log_level=logging.INFO):
    """
    Set up and configure a logger with the specified name and log level.
    
    Args:
        name (str): Name of the logger
        log_level (int): Logging level (e.g., logging.INFO, logging.DEBUG)
        
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Clear any existing handlers
    if logger.handlers:
        logger.handlers.clear()
    
    # Create file handler
    log_filename = f"{logs_dir}/ids_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(log_level)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.info(f"Logger initialized. Logs will be saved to {log_filename}")
    
    return logger

# Configure the logger
logger = setup_logger(log_level=logging.DEBUG)

def log_malicious_packet(packet_info):
    """Log details of a malicious packet."""
    logger.warning(f'Malicious packet detected: {packet_info}')

def log_benign_packet(packet_info):
    """Log details of a benign packet."""
    logger.info(f'Benign packet processed: {packet_info}')

def log_event(event_message):
    """Log general events."""
    logger.info(event_message)

# In your packet_sniffer.py, modify the sniff line:
# Define the network interface to sniff on
interface = "wlp0s20f3"  # Replace "eth0" with the appropriate interface name for your system

def packet_callback(packet):
    """
    Callback function to process sniffed packets.
    
    Args:
        packet: The sniffed packet object.
    """
    # Example logic to log packet details
    if "malicious" in str(packet):  # Replace with actual detection logic
        log_malicious_packet(packet.summary())
    else:
        log_benign_packet(packet.summary())

sniff(iface=interface, prn=packet_callback, store=False, filter="ip")