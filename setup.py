from distutils.core import setup
from sys import version
try:
	import py2exe
except ImportError:
	print "Warning: py2exe is not installed."
	print "(Though it may not be available on your platform.)"

requires = ['win32api']
if version < '2.6.0':
	requires.append("simplejson")


setup(
        name='Digital Clock',
        version='0.1',
        author='Shane Rees',
        url='http://github.com/Shaggs',
        console=['clock.py']
)