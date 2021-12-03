"""
Piston Code Runner API Wrapper
~~~~~~~~~~~~~~~~~~~
A simple api wrapper for Engineer Man's Piston API.
:copyright: (c) 2021 AalbatrossGuy
:license: MIT, see LICENSE.txt for more details.
"""
__title__ = "pistonpy"
__author__  = "AalbatrossGuy"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2021 AalbatrossGuy"

__all__ = ('PistonCli', 'PistonApp')
__path__ = __import__('pkgutil').extend_path(__path__, __name__)


from .pistonapp import *
from .pistoncli import *
