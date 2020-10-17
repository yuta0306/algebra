import sys

try:
    from . import core
    from .core import *

    __all__ = []
    __all__ += core.__all__

except ImportError:
    sys.stderr.write("Could not import algebra\n")

finally:
    del sys