from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as file:
    long_desc = file.read()

setup(
    name="pistonpy",
    version="0.0.2",
    description="An unofficial wrapper for Engineer Man's Piston API",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    python_requires = ">=3.8",
    package_dir={
        "pistonpy": "src/pistonpy",
    },
    packages=['pistonpy'],
    author="AalbatrossGuy",
    author_email="thexcelsiorisback@gmail.com",
    url="https://github.com/AaalbatrossGuy/pistonpy",
    install_requires=["requests", "typing"]
)
