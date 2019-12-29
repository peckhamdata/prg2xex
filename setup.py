"""Package code"""
from setuptools import setup, setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='prg2xex',
      version='0.0.3',
      description='Convert KickAssembler prg object code to Atari 8 Bit xex file',
      url='https://github.com/peckhamdata/prg2xex',
      author='worldofchris',
      author_email='chris@worldofchris.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      packages=setuptools.find_packages(),
      scripts=['bin/prg2xex'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"],
      install_requires=['pytest'],
      python_requires='>=3.6')
