import os
from urllib import request
import zipfile
from chicken_disease_classifier import logger
from chicken_disease_classifier.utils.common import get_size
from chicken_disease_classifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        
        self.config = config
        os.makedirs(self.config.root_dir,exist_ok=True)
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(url= self.config.source_URL, filename= self.config.local_data_file)
            logger.info(f"{filename} download! With Following info:\n {headers}")
        else:
            logger.info(f"File already Exists :{get_size(Path(self.config.local_data_file))}")
            
    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)