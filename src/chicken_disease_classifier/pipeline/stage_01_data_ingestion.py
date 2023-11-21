from chicken_disease_classifier.config.configuration import ConfigurationManager
from chicken_disease_classifier.components.data_ingestion import DataIngestion
from chicken_disease_classifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config= data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        


## if you want to run this stage separately
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    except Exception as e:
        logger.exception(e)
        raise e

