from setuptools import find_packages, setup  # type: ignore[reportMissingModuleSource]
from pathlib import Path
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements

    '''
    requirements = []
    requirements_path = Path(__file__).parent / file_path
    with open(requirements_path, encoding='utf-8') as file_obj:
        requirements = [
            requirement.strip()
            for requirement in file_obj
            if requirement.strip() and requirement.strip() != HYPEN_E_DOT
        ]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='lingaswamy',
    author_email='padire.lingaswamy321@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
