'''
Descripttion: your project
version: 1.0
Author: JiangFeng
Date: 2023-06-06 23:30:52
LastEditors: JiangFeng
LastEditTime: 2023-06-07 09:22:50
'''
from setuptools import setup
from setuptools import find_packages

VERSION = '0.2.0'

setup(
    name='emailmessage',
    version=VERSION,
    description='test setup tools and my basical functions.',
    packages=['emailmessage'],
    zip_safe=False,
    url='https://github.com/Wolf-Warriors-FDU/mail_message',
    author='Jiang Feng',
    author_email='jiangf21@m.fudan.edu.cn',
    # python_requires=">=3.7"
)