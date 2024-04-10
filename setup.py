from setuptools import setup, find_packages

setup(name="ASK API Test",
      version="1.0",
      install_packages=find_packages(),
      install_requires = [
          "pytest==8.1.1",
          "pymysql==1.1.0",
          "requests==2.31.0",
          "allure-pytest==2.13.5",
          "chardet==5.2.0"


          ]
    )