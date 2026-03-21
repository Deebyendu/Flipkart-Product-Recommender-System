from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Flipkart_recommendation_system",
    version="0.0.1",
    author="Deebyendu Mondal",
    packages=find_packages(),
    install_requires=requirements,
)