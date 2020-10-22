from .algebra import matrix
from ._overrides import set_module

from typing import TypeVar

T = TypeVar('T')

__all__ = ['asmatrix', 'aslist', 'astuple']

set_module('algebra')
def asmatrix(inputs: list) -> T:
    if isinstance(inputs, matrix):
        return inputs
    return matrix(inputs)

set_module('algebra')
def aslist(inputs: T) -> list:
    if isinstance(inputs, matrix):
        return inputs.data
    else:
        raise TypeError('Not supported type {}'.format(type(inputs)))

set_module('algebra')
def astuple(inputs: T) -> tuple:
    if isinstance(inputs, matrix):
        return tuple([
            tuple(row)
                for row in inputs.data
        ])
    else:
        raise TypeError('Not supported type {}'.format(type(inputs)))