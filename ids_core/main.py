import argparse
from ids_core.packet_sniffer import start_sniffing
from ids_core.utils.logger import setup_logger

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Intrusion Detection System')
    parser.add_argument('--interface', '-i', help='Network interface to sniff on')
    args = parser.parse_args()
    
    logger = setup_logger()
    logger.info("Starting the Intrusion Detection System...")
    
    try:
        start_sniffing(logger=logger, interface=args.interface)
    except KeyboardInterrupt:
        logger.info("Stopping the Intrusion Detection System...")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# In your packet_sniffer.py
def start_sniffing(logger, duration=3, interface=None):
    try:
        logger.info(f"Starting packet sniffing on interface: {interface or 'default'}")
        # Your sniffing code here
    except Exception as e:
        logger.error(f"Error during packet sniffing: {e}")
        # Re-raise or handle appropriately