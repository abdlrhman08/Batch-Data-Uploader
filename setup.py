from setuptools import setup, find_packages

'''Setuptools to be able to run the script globally without python'''
setup(
    name='uploader',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'sqlalchemy',
        'pandas'
    ],
    entry_points='''
        [console_scripts]
        uploader=uploader.uploader:cli
    ''',
)