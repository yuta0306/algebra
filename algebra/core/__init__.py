import sys
try:
    from . import algebra
    from .algebra import *
    from . import functions
    from .functions import *

    __all__ = ['matrix']
    __all__ += functions.__all__

except ImportError as e:
    sys.stderr.write("Import error\n")
    raise ImportError()

finally:
    del sys
