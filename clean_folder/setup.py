from setuptools import setup, find_namespace_packages


setup(
    name='clean_folder_olehV',
    version='1.2.2',
    description='sorted folder',
    url='https://github.com/OlehVakulchyk/goit_hw_7',
    author='Oleh Vakulchyk',
    author_email='4020405@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    data_files=[('clean_folder', ['main.py', 'normalize.py',
                 'subfunctions.py', 'start.py'])],
    include_package_data=True,
        entry_points={'console_scripts': [
            'clean-folder = clean_folder.main:start']}
)
