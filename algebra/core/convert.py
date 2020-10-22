from .algebra import matrix
from ._overrides import set_module

from typing import TypeVar

T = TypeVar('T')

__all__ = ['asmatrix', 'aslist', 'astuple']

set_module('algebra')
def asmatrix(inputs: list) -> T:
    return matrix(inputs)

set_module('algebra')
def aslist(inputs: T) -> list:
    return inputs.data

set_module('algebra')
def astuple(inputs: T) -> tuple:
    return tuple([
        tuple(row)
            for row in inputs.data
    ])