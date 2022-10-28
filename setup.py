from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Hugo Santos",
    author_email="hugosantosdev@gmail.com",
    description="leitor de imagem",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)