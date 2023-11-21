import os
from box.exceptions import BoxValueError
import yaml
from chicken_disease_classifier import logger
import json
import joblib
from ensure import ensure_annotations  ## Ensures the data type of parameters passed by Function.
from box import ConfigBox ## https://pypi.org/project/python-box/#:~:text=Box  See this you'll find the use of it.
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """ 
        reads YAML file and returns

        Args : path_to_yaml (str) -> path like input

        Returns : ConfigBox : ConfigBox type
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"{yaml_file} Loaded Successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('Yaml is Empty')
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories:list,verbose = True):
    """
        Create List of Directories 
    
        Args : path_to_directories(list): list of path of Directories
        ignore_log (bool,optional) : ignore if multiple dirs is to be created. Defaults to False

    """

    for path in path_to_directories:
        os.makedirs(path_to_directories,exist_ok=True)

        if verbose:
            logger.info(f'Created Directory at : {path}')

@ensure_annotations
def save_json(path:Path,data: dict):
    """
        Saves The JSON data
        Args : path(path) : path to Json file
               data(dict) : data to ve saved in json file
    """

    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logger.info(f'Json file saved at : {path}')


@ensure_annotations
def get_size(path: Path) -> str:
    """
        get size in KB

        Args:
            path (Path): path of the file

        Returns:
            str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    
    return f"~ {size_in_kb} KB"