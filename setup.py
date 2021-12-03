from setuptools import setup

with open("README.md") as file:
    long_desc = file.read()

setup(
    name="piston.py",
    version="0.0.1",
    description="An unofficial wrapper for Engineer Man's Piston API",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    package_dir={"piston.py": "src"},
    author="AalbatrossGuy",
    author_email="thexcelsiorisback@gmail.com",
    url="https://github.com/AaalbatrossGuy/piston.py",
    install_requires=["requests"]
)
