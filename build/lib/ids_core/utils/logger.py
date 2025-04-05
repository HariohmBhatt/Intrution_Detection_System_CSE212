from datetime import datetime
import logging

# Configure the logger
logging.basicConfig(
    filename='ids_core.log',  # Log file name
    level=logging.DEBUG,       # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def log_malicious_packet(packet_info):
    """Log details of a malicious packet."""
    logging.warning(f'Malicious packet detected: {packet_info}')

def log_benign_packet(packet_info):
    """Log details of a benign packet."""
    logging.info(f'Benign packet processed: {packet_info}')

def log_event(event_message):
    """Log general events."""
    logging.info(event_message)