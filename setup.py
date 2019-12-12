# coding:utf-8

from setuptools import setup, find_packages
from setuptools.dist import Distribution
from distutils.core import Extension
import os
import sys
import platform

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
     long_description = f.read()

# Init package is only for Windows so far

# if platform.system() == 'Windows':


if  sys.argv[-1] == 'init':

    # TODO1 : Check whether path contain chromedriver

    os.system("python ./src/dress.py")
    sys.exit()

    # TODO2 : Get all the platform suitable

setup(
        name='Dress',     
        version='1.0',   
        keywords = ["spider", "selenium", "python"],  
        description="a simple selenium snap up tool",  
        author='ttfish', 
        author_email="ttfish@protonmail.com",
        long_description_content_type="text/markdown",
        long_description = long_description,
        packages = find_packages(),
        url="https://github.com/fish98/Dress",
        platforms = "any", 
        install_requires = ['selenium'], 
        python_requires='>=3.6',
        classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        ],
        zip_safe=False               
)
