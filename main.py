from chicken_disease_classifier import logger
from chicken_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from chicken_disease_classifier.pipeline.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

except Exception as e:
    logger.exception(e)
    raise e 
    

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
except Exception as e:
    raise 

STAGE_NAME = "Model Training"
try:
    logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
except Exception as e:
    raise e

