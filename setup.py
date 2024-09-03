from setuptools import setup, find_packages

setup(
    name='fraud_transformer',
    python_requires='>=3.9',
    packages=find_packages("fraud_transformer"),
    install_requires=["kserve==0.12.1", "requests>=2.22.0", "numpy>=1.16.3"],
)
