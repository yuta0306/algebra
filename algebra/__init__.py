import sys

try:
    print('core')
    from . import core

    print(dir())

except ImportError:
    sys.stderr.write("Could not import algebra\n")

finally:
    del sys