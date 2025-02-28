from setuptools import find_packages, setup


with open("req.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="lung_cancer_pipeline",
    version="0.1",
    author="Rimjhim",
    description="A machine learning pipeline for lung cancer detection using CT scans.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,  # Installs dependencies from req.txt
)
