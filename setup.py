from setuptools import setup, find_packages

setup(
    name="email_assistant",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)