from pathlib import Path
import tensorflow as tf
from chicken_disease_classifier.entity.config_entity import ModelEvaluationConfig
from chicken_disease_classifier.utils.common import save_json
from chicken_disease_classifier import logger

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig) -> None:
        self.config = config

    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.2
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path:Path) -> tf.keras.models:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
    
    def save_score(self):
        scores = {'loss':self.score[0],'accuracy':self.score[1]}
        save_json(path= Path("scores.json"),data=scores)