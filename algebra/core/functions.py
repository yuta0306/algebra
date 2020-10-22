from typing import TypeVar

from .algebra import matrix
from ._overrides import set_module
from .convert import *

__all__ = ['zeros', 'zeros_like', 'ones', 'ones_like', 'is_square', 'is_symmetric',
            'is_diagonal', 'is_vector', 'is_zerovec']

T = TypeVar('T')

@set_module('algebra')
def zeros(shape: list or tuple) -> T:
    """
    >>> import algebra as alg
    >>> a = alg.zeros((2, 2))
    >>> a
    matrix([
            [0, 0]
            [0, 0]
        ])

    >>> b = alg.zeros([2, 2])
    >>> b
    matrix([
            [0, 0]
            [0, 0]
        ])

    >>> c = alg.zeros((2, 4))
    >>> c
    matrix([
            [0, 0, 0, 0]
            [0, 0, 0, 0]
        ])

    >>> d = alg.zeros(2)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "your-path/algebra/algebra/core/functions.py", line 20, in zeros
        raise TypeError('Not supported type {}'.format(type(shape)))
    TypeError: Not supported type <class 'int'>
    
    """
    if isinstance(shape, (tuple, list)):
        try:
            return matrix([
                [0 for _ in range(shape[1])]
                    for _ in range(shape[0])
            ])
        except ValueError:
            raise ValueError('expect the shape (int, int) and the length is 2, but {} and {}'.format(shape, len(shape)))
    else:
        raise TypeError('Not supported type {}'.format(type(shape)))

@set_module('algebra')
def zeros_like(inputs: T) -> T:
    """
    >>> a = alg.matrix([[1, 2], [3, 4]])
    >>> a
    matrix([
            [1, 2]
            [3, 4]
        ])

    >>> b = alg.zeros_like(a)
    >>> b
    matrix([
            [0, 0]
            [0, 0]
        ])

    """
    try:
        inputs = asmatrix(inputs)
        return matrix([
            [0 for _ in range(inputs.column)]
                for _ in range(inputs.row)
        ])
    except TypeError:
        raise TypeError('Not supprted type {}'.format(type(inputs)))

@set_module('algebra')
def ones(shape: list or tuple) -> T:
    """
    >>> import algebra as alg
    >>> a = alg.ones((2, 2))
    >>> a
    matrix([
            [1, 0]
            [0, 1]
        ])

    >>> b = alg.ones([2, 2])
    >>> b
    matrix([
            [1, 0]
            [0, 1]
        ])

    >>> c = alg.ones((2, 4))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "your-path/algebra/algebra/core/functions.py", line 41, in ones
        
    ValueError: expect the shape (2, 2), but (2, 4)

    >>> d = alg.ones(2)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "your-path/algebra/algebra/core/functions.py", line 20, in zeros
        raise TypeError('Not supported type {}'.format(type(shape)))
    TypeError: Not supported type <class 'int'>
    
    """
    if isinstance(shape, (tuple, list)):
        if shape[0] == shape[1]:
            return matrix([
                [0 if not i==j else 1 for j in range(shape[1])]
                    for i in range(shape[0])
            ])
        else:
            raise ValueError('expect the shape ({0}, {0}), but {1}'.format(shape[0], shape))
    else:
        raise TypeError('Not supported type {}'.format(type(shape)))

@set_module('algebra')
def ones_like(inputs: T) -> T:
    """
    >>> a = alg.matrix([[1, 2], [3, 4]])
    >>> a
    matrix([
            [1, 2]
            [3, 4]
        ])

    >>> b = alg.zeros_like(a)
    >>> b
    matrix([
            [1, 0]
            [0, 1]
        ])

    >>> c = alg.matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    >>> c
    matrix([
            [1, 2, 3, 4]
            [5, 6, 7, 8]
        ])

    >>> d = alg.ones_like(c)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "your-path/algebra/algebra/core/functions.py", line 54, in ones_like
        @set_module('algebra')
    ValueError: expect the shape (2, 2), but (2, 4)
    """
    try:
        inputs = asmatrix(inputs)
        if inputs.row == inputs.column:
            return matrix([
                [0 if not i==j else 1 for i in range(inputs.column)]
                    for j in range(inputs.row)
            ])
        else:
            raise ValueError('expect the shape ({0}, {0}), but {1}'.format(inputs.row, inputs.shape))
    except TypeError:
        raise TypeError('Not supprted type {}'.format(type(inputs)))

@set_module('algebra')
def is_square(inputs: T) -> bool:
    try:
        inputs = asmatrix(inputs)
        row = inputs.row
        col = inputs.column
        if row == col:
            return True
        else:
            return False
    except TypeError:
        raise TypeError('expect type matrix, but {}'.format(type(inputs)))

@set_module('algebra')
def is_symmetric(inputs: T) -> bool:
    try:
        inputs = asmatrix(inputs)
        if is_square(inputs):
            return inputs == inputs.T
        else:
            raise TypeError('expect the shape ({0}, {0}), but {1}'.format(inputs.row, inputs.shape))

    except TypeError:
        raise TypeError('expect type matrix, but {}'.format(type(inputs)))

@set_module('algebra')
def is_diagonal(inputs: T) -> bool:
    try:
        inputs = asmatrix(inputs)
        if is_square(inputs):
            row = inputs.row
            col = inputs.column
            for i in range(row):
                for j in range(col):
                    if i != j and inputs[i][j] != 0:
                        return False
            return True
        else:
            raise TypeError('expect the shape ({0}, {0}), but {1}'.format(inputs.row, inputs.shape))
    except TypeError:
        raise TypeError('expect type matrix, but {}'.format(type(inputs)))

@set_module('algebra')
def is_vector(inputs: T) -> bool:
    try:
        inputs = asmatrix(inputs)
        return inputs.is_vector
    except TypeError:
        raise TypeError('expect type matrix, but {}'.format(type(inputs)))

@set_module('algebra')
def is_zerovec(inputs: T) -> T:
    try:
        inputs = asmatrix(inputs)
        if is_vector(inputs):
            for row in inputs.data:
                for col in row:
                    if not col == 0:
                        return False
            else:
                return True
        else:
            return False
    except TypeError:
        raise TypeError('expect type matrix, but {}'.format(type(inputs)))