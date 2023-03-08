from setuptools import find_packages, setup
from typing import List

HYPEN_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will reurn a list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)

    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Vachan',
    author_email = 'vachanshetty95@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = get_requirements('requirements.txt')
    )