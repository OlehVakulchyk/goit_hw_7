from setuptools import setup, find_namespace_packages


setup(
    name='clean_folder',
    version='1.1.0',
    description='sorted folder',
    url='https://github.com/OlehVakulchyk/goit_hw_7',
    author='Oleh Vakulchyk',
    author_email='4020405@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
        entry_points={'console_scripts': [
        'clean-folder = clean_folder.main:start']}
)
