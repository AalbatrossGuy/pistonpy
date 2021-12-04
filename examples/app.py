from pistonpy import PistonApp
import requests, json

# Initialize the client.
piston = PistonApp()

my_code = "print('This code ran from app.py itself!')"

output = piston.run(language="python", version="3.10.0", code=my_code)

print(output)

# Output: {'language': 'python', 'version': '3.10.0', 'run': {'stdout': 'This code ran from app.py itself!\n', 'stderr': '', 'code': 0, 'signal': None, 'output': 'This code ran from app.py itself!\n'}}

run_file = piston.run(language="python", files=['test.py']) # version is optional. files even if it maybe only one must be given as lists.

print(run_file)

# Output: {'language': 'python', 'version': '3.10.0', 'run': {'stdout': 'The code ran from test.py\n', 'stderr': '', 'code': 0, 'signal': None, 'output': 'The code ran from test.py\n'}}

# You cannot provide both code and files in a single PistonAPP().run() instance.
