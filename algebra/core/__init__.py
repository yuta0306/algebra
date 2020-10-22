import sys
try:
    from . import algebra
    from .algebra import *
    from . import functions
    from .functions import *
    from . import convert
    from .convert import *

    __all__ = ['matrix']
    __all__ += functions.__all__
    __all__ += convert.__all__

except ImportError as e:
    msg = (
        "Catch Import error: "
        "There are some problems in algebra.py or functions.py\n"
        )
    sys.stderr.write(msg)
    raise ImportError()

finally:
    del sys
