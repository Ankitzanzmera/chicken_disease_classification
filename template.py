import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[ %(asctime)s ] : %(message)s : ')

project_name = "chicken-disease-classifier"

list_of_file = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "notebooks/trials.ipynb",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_file:
    filepath = Path(filepath)   ## returns path which is recognize as windows path
    dirname,filename = os.path.split(filepath)

    if dirname != "":
        os.makedirs(dirname,exist_ok=True)
        logging.info(f'{dirname} folder is created..')

    if (not os.path.exists(filepath)) or (os.path.getsize == 0):
        with open(filepath,"wb"):
            pass
        logging.info(f'{filepath} file is created..')

    else:
        logging.info(f'{filepath} is Alreasy Exists')
