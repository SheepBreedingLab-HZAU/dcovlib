# coding: utf-8

from setuptools import setup

REQUIRES = ["numpy"]

setup(
    name='dcovlib',
    version='1.0.0',
    python_requires='>=3.6',
    description='convert numpy to ird file, or convert ird to numpy',
    platforms='Independant',
    author='Sun ling', # 作者
    author_email="ling.sun-01@qq.com",
    author_lab="sheep breeding Lab from huazhong agricultural university",
    url="https://github.com/SheepBreedingLab-HZAU/dcovlib",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES,
    packages=['dcovlib']
)

