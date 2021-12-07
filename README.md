<h1 align="center">Pistonpy</h1>
<p align="center">
    <a href="https://pypi.org/project/pistonpy/0.0.3/">
        <img src="https://img.shields.io/pypi/v/pistonpy.svg?style=for-the-badge&color=orange&logo=&logoColor=white" />
    </a>
    <a href="https://github.com/AalbatrossGuy/pistonpy/commits/v0.0.2">
        <img src="https://img.shields.io/github/commits-since/AalbatrossGuy/pistonpy/v0.0.2?style=for-the-badge" />
    </a>
    <a>
    <a href="https://app.codacy.com/gh/AalbatrossGuy/pistonpy/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AalbatrossGuy/pistonpy&amp;utm_campaign=Badge_Grade">
        <img src="https://img.shields.io/codacy/grade/d54121e3fbc94d4195d9c9e3791fbe47?style=for-the-badge" />
    </a>
    <br> Pistonpy is an API wrapper for the Piston code execution engine by Engineer Man.
</p>

## Key Features
* Simple modern and efficient Pythonic API using the `requests` lib.
* Supports application integration and CLI usage.

## Requirements

Python 3.8+
* [requests](https://pypi.org/project/requests/)

## Installing
To install the library, run the following commands:
```shell
# Linux/MacOS
python3 -m pip install -U pistonpy

# Windows
py -3 -m pip install -U pistonpy
```

## Usage

```python
from pistonpy import PistonApp

# Initialize the client.
piston = PistonApp()

my_code = "print('This code ran from app.py itself!')"

output = piston.run(language="python", version="3.10.0", code=my_code)

print(output)
```
This gives the output:
```python
{'language': 'python', 'version': '3.10.0', 'run': {'stdout': 'This code ran from app.py itself!\n', 'stderr': '', 'code': 0, 'signal': None, 'output': 'This code ran from app.py itself!\n'}}
```

```python
run_file = piston.run(language="python", files=['test.py']) # version is optional. files even if it maybe only one must be given as lists.

print(run_file)
```
This gives the same output,
```python
{'language': 'python', 'version': '3.10.0', 'run': {'stdout': 'The code ran from test.py\n', 'stderr': '', 'code': 0, 'signal': None, 'output': 'The code ran from test.py\n'}}
```

```python
# You cannot provide both code and files in a single PistonAPP().run() instance.

# For running multiple files (For now it ONLY supports multiple python files)

multiple_files = piston.run(language="python", version="3.10.0", files=['test.py', 'test_two.py'])

print(multiple_files)
```
Sadly, the output for multiple files are provided all-together. This will be fixed in the upcoming updates. The above statement will output to:
```python
{'language': 'python', 'version': '3.10.0', 'run': {'stdout': 'The code ran from test.py\nthis is test 2\n', 'stderr': '', 'code': 0, 'signal': None, 'output': 'The code ran from test.py\nthis is test 2\n'}}
```

```python
print(piston.languages) # Prints the available languages along with their version.

print(piston.aliases) # Prints the available languages along with their alias/aliases.

print(piston.raw) # Prints the raw data without any formatting done.
```

## License

This project is distributed under the [MIT](https://github.com/AalbatrossGuy/pistonpy/blob/main/LICENSE) license.

## Piston

For visiting Piston's github repository, [click here.](https://github.com/engineer-man/piston)
