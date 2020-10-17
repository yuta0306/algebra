import sys
try:
    print('functions')
    from . import *

    print(dir())

except ImportError:
    sys.stderr.write("Import error")
    raise ImportError()

finally:
    del sys