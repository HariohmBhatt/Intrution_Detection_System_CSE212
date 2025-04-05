from scapy.all import sniff
from ids_core.notifications.email_notifier import send_email_notification
from ids_core.utils.logger import log_event

def packet_callback(packet):
    # Logic to analyze the packet and determine if it's malicious
    if is_malicious(packet):
        log_event("Malicious packet detected!")
        send_email_notification(
            recipient="user@example.com",
            subject="Malicious Packet Detected",
            message=f"A malicious packet has been detected: {packet.summary()}"
        )

def is_malicious(packet):
    # Placeholder for actual malicious packet detection logic
    # This should analyze the packet and return True if it's malicious
    return False

def start_sniffing():
    sniff(prn=packet_callback, timeout=3)

if __name__ == "__main__":
    start_sniffing()