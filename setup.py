from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:

    requirements = []

    hypen_e = '-e .'
    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n',"")   for req in requirements]
        if hypen_e in requirements:
            requirements.remove(hypen_e)
        
        
        



setup(
    name='ml_project',
    version="0.0.1",
    author='rishi',
    author_email='singhmanharsh92@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


if __name__ =="__main__":
    get_requirements('requirements.txt')