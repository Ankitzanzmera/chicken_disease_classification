import os
from urllib import request
from zipfile import ZipFile
import tensorflow as tf
import time
from chicken_disease_classifier.entity.config_entity import PrepareCallbacksConfig

class PrepareCallback:
    def __init__(self,config:PrepareCallbacksConfig) -> None:
        self.config = config

    @property
    def _create_tensorboard(self):
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
        tb_running_log_dir = os.path.join(self.config.tensorboard_root_log_dir,f"tb_logs_at_{timestamp}")

        return tf.keras.callbacks.TensorBoard(log_dir= tb_running_log_dir)
    
    @property
    def _create_checkpoint_model(self):
        return tf.keras.callbacks.ModelCheckpoint(filepath=self.config.checkpoint_model_filepath,save_best_only=True)
    
    def create_ckpt_callbacks(self):
        return [self._create_tensorboard,self._create_checkpoint_model]