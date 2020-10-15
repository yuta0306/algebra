from typing import TypeVar, Generic
T = TypeVar('T')

class matrix(Generic[T]):
    def __init__(self, data: list):
        if not isinstance(data, list):
            raise TypeError('Not supported type {}.'.format(type(data)))

        _row = len(data)
        _column = None
        _is_vector = False
        for elm in data:
            if isinstance(elm, int) or isinstance(elm, float):
                _is_vector = True
            else:
                _is_vector = False
        if _is_vector:
            data = [data]
            _row = 1

        for inner in data:
            for elm in inner:
                if not isinstance(elm, int) or isinstance(elm, float):
                    raise TypeError('{} is not matrix.'.format(data))
            if _column is None:
                _column = len(inner)
            else:
                compare = len(inner)
                if not _column == compare:
                    raise TypeError('{} is not matrix'.format(data))
                _column = compare
        
        self._data = data
        self._row = _row
        self._column = _column
        self._shape = _row, _column

                
    def __repr__(self):
        p = '['
        for row in self.data:
            p += '\n         ' + str(row)
        p += '\n       ]'
        return 'matrix({})\n'.format(p)

    def __len__(self):
        return len(self.data)

    def __add__(self, other: T) -> T:
        if isinstance(other, matrix):
            if self.shape == other.shape:
                return matrix([
                    [x + y for x, y in zip(X, Y)]
                        for X, Y in zip(self.data, other.data)
                ])
            else:
                raise ValueError('Shape: {} does not equal to {}.'.format(self.shape, other.shape))
        else:
            raise TypeError('cannot add {} to {}.'.format(type(self), type(other)))

    def  __radd__(self, other: T) -> T:
        if isinstance(other, matrix):
            if other.shape == self.shape:
                return matrix([
                    [x + y for x, y in zip(X, Y)]
                        for X, Y in zip(other.data, self.data)
                ])
            else:
                raise ValueError('Shape: {} does not equal to {}.'.format(other.shape, self.shape))
        else:
            raise TypeError('cannot add {} to {}.'.format(type(other), type(self)))

    def __sub__(self, other: T) -> T:
        if isinstance(other, matrix):
            if self.shape == other.shape:
                return matrix([
                    [x - y for x, y in zip(X, Y)]
                        for X, Y in zip(self.data, other.data)
                ])
            else:
                raise ValueError('Shape: {} does not equal to {}.'.format(self.shape, other.shape))
        else:
            raise TypeError('cannot subtract {} from {}.'.format(type(other), type(self)))

    def __rsub__(self, other: T) -> T:
        if isinstance(other, matrix):
            if other.shape == self.shape:
                return matrix([
                    [x - y for x, y in zip(X, Y)]
                        for X, Y in zip(other.data, self.data)
                ])
            else:
                raise ValueError('Shape: {} does not equal to {}.'.format(other.shape, self.shape))
        else:
            raise TypeError('cannot subtract {} from {}.'.format(type(self), type(other)))

    def __mul__(self, other: T) -> T:
        if isinstance(other, matrix):
            if self.shape[0] == other.shape[1]:
                return matrix([
                    [
                        sum([
                            x * y for x, y in zip(X, Y)
                        ])
                        for Y in other.T
                    ]
                    for X in self.data
                ])
            else:
                raise ValueError('Shape: expect input shape ({}, any) and (any, {}), but {} and {}'.format(
                                    self.shape[0], self.shape[0], self.shape, other.shape))
            
        else:
            raise TypeError('cannot multiply {} and {}.'.format(type(self), type(other)))

    def __rmul__(self, other: int or float) -> T:
        if isinstance(other, int) or isinstance(other, float):
            return matrix([
                [other * x for x in X]
                    for X in self.data
            ])
        elif isinstance(other, matrix):
            if self.shape[0] == other.shape[1]:
                return matrix([
                    [
                        sum([
                            x * y for x, y in zip(X, Y)
                        ])
                        for Y in self.T
                    ]
                    for X in other
                ])
            else:
                raise ValueError('Shape: expect input shape ({}, any) and (any, {}), but {} and {}'.format(
                                    self.shape[1], self.shape[1], other.shape, self.shape))
            
        else:
            raise TypeError('cannot multiply {} and {}.'.format(type(other), type(self)))

    def __truediv__(self, other: any):
        raise TypeError('cannot use operator (/) for matrix')

    def __rtruediv__(self, other: any):
        raise TypeError('cannot use operator (/) for matrix')

    def __eq__(self, other: any) -> bool:
        return self._data == other._data

    @property
    def data(self):
        return self._data

    @data.deleter
    def data(self):
        self._data = None
        self._row = None
        self._column = None
        self._shape = None

    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._column

    @property
    def shape(self) -> tuple:
        return self._shape

    @property
    def T(self) -> T:
        return matrix([
                list(row) for row in zip(*self._data)
            ])


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

def zeros_like(inputs: T) -> T:
    if isinstance(inputs, matrix):
        return matrix([
            [0 for _ in range(inputs.column)]
                for _ in range(inputs.row)
        ])
    else:
        raise TypeError('Not supprted type {}'.format(type(inputs)))

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

def is_symmetric(inputs: T) -> bool:
    if isinstance(inputs, matrix):
        return True if inputs == inputs.T else False
    else:
        raise TypeError('expect type matrix, but {}'.format(type(inputs)))