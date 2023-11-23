from chicken_disease_classifier.config.configuration import ConfigurationManager
from chicken_disease_classifier.components.prepare_callback import PrepareCallback
from chicken_disease_classifier.components.model_training import ModelTraining
from chicken_disease_classifier import logger

STAGE_NAME = "Model Training"

class ModelTrainingPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            callback_config = config.get_prepare_callbacks_config()
            prepare_callback = PrepareCallback(config=callback_config)
            callback_list = prepare_callback.create_ckpt_callbacks()

            training_config = config.get_model_training_config()
            training = ModelTraining(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train_model(callback_list=callback_list)
            
        except Exception as e:
            raise e         

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    except Exception as e:
        raise e