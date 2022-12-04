from setuptools import setup, find_namespace_packages
from setuptools import setup, find_packages

setup(
    
    version='0.1.0',
    packages=find_packages(include=['exampleproject', 'exampleproject.*'])
)


setup(
    name='clean_folder',
    version='0.1.0',
    description='sorted folder',
    url='http://github.com/dummy_user/useful',
    author='Oleh Vakulchyk',
    author_email='4020405@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'sortfolder = clean_folder.main:main']}
)
