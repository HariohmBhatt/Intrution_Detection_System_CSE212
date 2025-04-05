from scapy.all import sniff, IP
from ids_core.notifications.email_notifier import send_email_notification
from ids_core.utils.logger import log_event
from ids_core.packet_analyzer import analyze_packet

def process_packet(packet, logger=None):
    if logger:
        logger.info(f"Processing packet: {packet.summary()}")  # Changed from debug to info
    return analyze_packet(packet, logger)

def start_sniffing(logger, duration=3, interface=None):
    try:
        logger.info(f"Starting packet sniffing on interface: {interface or 'default'}")
        
        # Initialize counters
        packet_count = 0
        malicious_count = 0
        
        # Define callback for packet processing
        def packet_callback(packet):
            nonlocal packet_count, malicious_count
            if IP in packet:  # Only process IP packets
                packet_count += 1
                logger.info(f"Captured packet #{packet_count}: {packet.summary()}")
                if process_packet(packet, logger):
                    malicious_count += 1
        
        # Start continuous sniffing
        logger.info("Starting continuous packet capture. Press Ctrl+C to stop...")
        sniff(iface=interface, prn=packet_callback, store=False)
        
    except KeyboardInterrupt:
        logger.info("Packet sniffing stopped by user")
        logger.info(f"Processed {packet_count} packets, {malicious_count} were malicious")
    except Exception as e:
        logger.error(f"Error during packet sniffing: {e}")
        raise

if __name__ == "__main__":
    start_sniffing()