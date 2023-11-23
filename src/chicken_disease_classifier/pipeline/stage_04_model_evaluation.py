from chicken_disease_classifier.config.configuration import ConfigurationManager
from chicken_disease_classifier.components.model_evaluation import ModelEvaluation
from chicken_disease_classifier import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            evaluation_config = config.get_validation_config()
            evaluate_model = ModelEvaluation(config=evaluation_config)
            evaluate_model.evaluation()
            evaluate_model.save_score()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    except Exception as e:
        raise e


