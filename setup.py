from setuptools import setup,find_packages
from typing import List

def get_requirements(filename) -> List:
    requirements = []
    HYPHEN_E_DOT = "-e ."

    with open(filename,"r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = "chicken_disease_classification",
    version = "0.0.1",
    author= "Ankit Zanzmera",
    author_email= "22msrds052@jainuniversity.ac.in",
    description = "A small project that classfies the disease of chicken",
    packages = find_packages(where="src"),
    package_dir={"": "src"},
    url = "https://github.com/Ankitzanzmera/chicken_disease_classification",
)