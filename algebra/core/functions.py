import os
import sys

from .algebra import matrix
from ._overrides import set_module

T = matrix

@set_module('algebra')
def zeros(shape: list or tuple) -> T:
    if isinstance(shape, list) or isinstance(shape, tuple):
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
    if isinstance(inputs, matrix):
        return matrix([
            [0 for _ in range(inputs.column)]
                for _ in range(inputs.row)
        ])
    else:
        raise TypeError('Not supprted type {}'.format(type(inputs)))

@set_module('algebra')
def ones(shape: list or tuple) -> T:
    if isinstance(shape, list) or isinstance(shape, tuple):
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
    if isinstance(inputs, matrix):
        if inputs.row == inputs.column:
            return matrix([
                [0 if not i==j else 1 for i in range(inputs.column)]
                    for j in range(inputs.row)
            ])
        else:
            raise ValueError('expect the shape ({0}, {0}), but {1}'.format(inputs.row, inputs.shape))
    else:
        raise TypeError('Not supprted type {}'.format(type(inputs)))

@set_module('algebra')
def is_square(inputs: T) -> bool:
    if isinstance(inputs, matrix):
        row = inputs.row
        col = inputs.column
        if row == col:
            return True
        else:
            return False
    else:
        raise TypeError('expect type matrix, but {}'.format(type(inputs)))

@set_module('algebra')
def is_symmetric(inputs: T) -> bool:
    if isinstance(inputs, matrix):
        if is_square(inputs):
            return inputs == inputs.T
        else:
            raise TypeError('expect the shape ({0}, {0}), but {1}'.format(inputs.row, inputs.shape))

    else:
        raise TypeError('expect type matrix, but {}'.format(type(inputs)))

@set_module('algebra')
def is_diagonal(inputs: T) -> bool:
    if isinstance(inputs, matrix):
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
    else:
        raise TypeError('expect type matrix, but {}'.format(type(inputs)))

__all__ = ['zeros', 'zeros_like', 'ones', 'ones_like', 'is_square', 'is_symmetric',
            'is_diagonal']