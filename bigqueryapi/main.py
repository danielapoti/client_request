import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting script execution")


def main():
    logging.info("In main")


if __name__ == "__main__":
    logging.info("Starting the machine!")
    main()
