import logging

# Cấu hình logging

logging.basicConfig(filename='./vireader',
                filemode='w',
                encoding='utf-8',                             
                level=logging.INFO,
                format="%(asctime)s:%(levelname)s:%(funcName)s: %(message)s",
                datefmt='%H:%M:%S')

# logging.basicConfig(
#     level=logging.WARNING,  # Mức logging mặc định
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S"
# )

# Sử dụng logger
logger = logging.getLogger("example_logger")

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
