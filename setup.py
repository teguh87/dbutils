from setuptools import setup, find_packages

setup(
    name='dbutils',
    version="0.1",
    packages=find_packages(exclude=['contrib', 'docs', 'example']),
    # installed or upgraded on the target machine
    install_requires=['psycopg2>=2.5.2', 'SQLAlchemy>=1.3.1'],
    author="Teguh Santoso",
    author_email='teguhdev87@gmail.com',
    description='This utils for sqlalchemy utils',
    license='Apache',
    keywords='sqlalchemy, psycopg2',
)
