# This setup.py file is for builiding our application as a package itself. we can deploy this package in python PyPi(Python package index - it's repository where there's different packages of python such as seaborn,pandas) and from there anybody can do the installation of that package and use it.

#automatically find all packages that required
from setuptools import find_packages,setup  
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# Creating parameters that required
setup(
name='mlproject',
version='0.0.1', 
author='sanjeevani',
author_email='sanjeevanipawar7@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)
