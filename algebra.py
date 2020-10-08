class matrix:
    def __init__(self, data: list):
        if not isinstance(data, list):
            raise TypeError('Not supported type {}.'.format(type(data)))

        depth = 0
        row = len(data)
        column = None
        if isinstance(data[0], int) or isinstance(data[0], float):
            column = 1
        else:
            for inner in data:
                for elm in inner:
                    if not isinstance(elm, int) or isinstance(elm, float):
                        raise TypeError('{} is not matrix.'.format(data))
                if column is None:
                    column = len(inner)
                else:
                    compare = len(inner)
                    if not column == compare:
                        raise TypeError('{} is not matrix'.format(data))
                    column = compare
        
        self.data = data
        self.shape = row, column

                
    def __repr__(self):
        return 'matrix({})'.format(self.data)

    def __add__(self, other: matrix) -> matrix:
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

    def  __radd__(self, other: matrix) -> matrix:
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

    def __sub__(self, other: matrix) -> matrix:
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

    def __rsub__(self, other: matrix) -> matrix:
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
