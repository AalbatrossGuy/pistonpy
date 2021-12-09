from pistonpy import PistonApp

# Initialize the client.
piston = PistonApp()

my_code = "print('This code ran from app.py itself!')"

#output = piston.run(language="python", version="3.10.0", code=my_code)

#print(output)
# Output: {'language': 'python', 'version': '3.10.0', 'run': {'stdout': 'This code ran from app.py itself!\n', 'stderr': '', 'code': 0, 'signal': None, 'output': 'This code ran from app.py itself!\n'}}

#run_file = piston.run(language="python", files=['test.py']) # version is optional. files even if it maybe only one must be given as lists.

#print(run_file)

# Output: {'language': 'python', 'version': '3.10.0', 'run': {'stdout': 'The code ran from test.py\n', 'stderr': '', 'code': 0, 'signal': None, 'output': 'The code ran from test.py\n'}}

# You cannot provide both code and files in a single PistonAPP().run() instance.

# For running multiple files (For now it ONLY supports multiple python files)

multiple_files = piston.run(language="java", version="15.0.2", files=['test.java', 'test_two.java'])
#
print(multiple_files)

# Output: {'language': 'python', 'version': '3.10.0', 'run': {'stdout': 'The code ran from test.py\nthis is test 2\n', 'stderr': '', 'code': 0, 'signal': None, 'output': 'The code ran from test.py\nthis is test 2\n'}}

# print(piston.languages) # Prints the available languages along with their version.
#
# print(piston.aliases) # Prints the available languages along with their alias/aliases.
#
# print(piston.raw) # Prints the raw data without any formatting done.
