from setuptools import setup, find_packages

setup (name="census-income",
       version="0.0.1",
       author="devesh",
       author_email="deveshmaan7@gmail.com",
       packages=find_packages(),
       install_requires=["pandas","numpy","flask"]
)