import logging
import os,sys
from datetime import datetime

log_dir_name = f"{datetime.now().strftime('%d_%m_%y')}"
log_dir_path = os.path.join(os.getcwd(),"logs",log_dir_name)
os.makedirs(log_dir_path,exist_ok=True)

log_file_name = f'{datetime.now().strftime("%H_%M_%S.log")}'
log_file_path = os.path.join(log_dir_path,log_file_name)


logging.basicConfig(
    level=logging.INFO,
    format= "[ %(asctime)s ] %(lineno)d - %(module)s - %(levelname)s - %(message)s",
    handlers= [
        logging.FileHandler(log_file_path), 
        logging.StreamHandler(sys.stdout)
        ]
)
logger = logging.getLogger("classifierlogger")
