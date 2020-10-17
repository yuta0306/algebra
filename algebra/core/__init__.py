import sys
try:
    import algebra
    print('functions')
    from .  import functions

    print(dir())

except ImportError:
    sys.stderr.write("Import error")
    raise ImportError()

finally:
    del sys
