class matrix:
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
        self._shape = _row, _column
        self._T = [
            list(row) for row in zip(*data)
        ]

                
    def __repr__(self):
        return 'matrix({})'.format(self.data)

    def __add__(self, other):
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

    def  __radd__(self, other):
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

    def __sub__(self, other):
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

    def __rsub__(self, other):
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

    def __mul__(self, other):
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

    def __rmul__(self, other):
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

    def __div__(self, other):
        raise TypeError('cannot use operator (/) for matrix')

    def __rdiv__(self, other):
        raise TypeError('cannot use operator (/) for matrix')

    @property
    def data(self):
        return self._data

    @data.deleter
    def data(self):
        self._data = None
        self._shape = None
        self._T = None

    @property
    def shape(self):
        return self._shape

    @property
    def T(self):
        return self._T