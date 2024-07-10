from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    with open(file_path) as requirement_file:
        requirements = requirement_file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name='End-to-End-ML-Project',
version='0.0.1',
author='Hamza',
author_email='muhammadhamzasabir752@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)