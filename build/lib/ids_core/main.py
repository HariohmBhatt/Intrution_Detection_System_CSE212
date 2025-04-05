from ids_core.packet_sniffer import start_sniffing
from ids_core.utils.logger import setup_logger

def main():
    logger = setup_logger()
    logger.info("Starting the Intrusion Detection System...")
    
    try:
        start_sniffing()
    except KeyboardInterrupt:
        logger.info("Stopping the Intrusion Detection System...")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()