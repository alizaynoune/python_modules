class Vector:
    def __init__(self, values) -> None:
        self.values = [[]]
        if isinstance(values, list) and isinstance(values[0], list):
            val_len = len(values)
            if val_len == 1 and not len(values[0]):
                raise ValueError('error is empty')
            for i in values[0] if val_len == 1 else values:
                if val_len != 1:
                    if not isinstance(i, list) or not len(i) == 1 or \
                            not isinstance(i[0], float):
                        raise ValueError(
                            'error The values can be only float {}'.format(i))
                else:
                    if not isinstance(i, float):
                        raise ValueError(
                            'error The values can be only float {}'.format(i))

            self.values = values[:]
            self.shape = (val_len, len(values[0]))
        elif isinstance(values, int):
            if values <= 0:
                raise ValueError(
                    'error value cannot be negative {}'.format(values))
            self.shape = (values, 1)
            self.values = [[float(i)] for i in range(values)]
        elif isinstance(values, tuple):
            if not all(isinstance(i, int) for i in values):
                raise ValueError(
                    'error the values can be only integers {}'.format(values))
            if len(values) != 2 or values[0] < 0 or values[0] >= values[1]:
                raise ValueError(
                    'error the start cannot be less than or equal the end {}'
                    .format(values))
            self.shape = (values[1] - values[0], 1)
            self.values = [[float(i)] for i in range(values[0], values[1])]
        else:
            raise ValueError('error type of {}'.format(values))

        pass

    def __add__(self, vec):
        if not isinstance(vec, Vector) or self.shape != vec.shape:
            raise ValueError("Vectors must have the same dimensions.")

        if vec.shape[0] >= vec.shape[1]:
            return Vector(
                [[a[0] + b[0]] for (a, b) in zip(self.values, vec.values)])
        else:
            return Vector(
                [[a[0] + b[0] for (a, b) in zip(self.values, vec.values)]])

    def __radd__(self, vec):
        # add & radd : only vectors of same shape.
        return self.__add__(vec)

    def __sub__(self, vec):
        if not isinstance(vec, Vector) or self.shape != vec.shape:
            raise ValueError("Vectors must have the same dimensions.")
        if vec.shape[0] >= vec.shape[1]:
            return Vector(
                [[a[0] * b[0]] for (a, b) in zip(self.values, vec.values)])
        else:
            return Vector(
                [[a[0] * b[0] for (a, b) in zip(self.values, vec.values)]])

    def __rsub__(self, vec):
        # sub & rsub: only vectors of same shape.
        return self.__sub__(vec)

    def __truediv__(self, scalar):
        # truediv :
        # only with scalars (to perform division of Vector by a scalar).
        if not isinstance(scalar, (int, float)):
            raise ValueError('Scalar must be int or float')
        if scalar == 0:
            raise ZeroDivisionError('division by zero.')
        res = Vector(self.values)
        if res.shape[0] >= res.shape[1]:
            res.values = [[j / scalar] for i in res.values for j in i]
        else:
            res.values = [[j / scalar for i in res.values for j in i]]
        return res

    def __rtruediv__(self, value):
        # rtruediv :
        # raises an NotImplementedError with the message
        # "Division of a scalar by a Vector is not defined here."
        raise NotImplementedError(
            'Division of a scalar by a Vector is not defined here.')

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError('Scalar must be int or float')
        res = Vector(self.values)
        if res.shape[0] >= res.shape[1]:
            res.values = [[j * scalar] for i in res.values for j in i]
        else:
            res.values = [[j * scalar for i in res.values for j in i]]

        return res

    def __rmul__(self, scalar):
        # mul & rmul:
        # only scalars (to perform multiplication of Vector by a scalar).
        return self.__mul__(scalar)

    def __str__(self):
        return f'Vector({self.values})'

    def __repr__(self):
        # must be identical, i.e we expect that print(vector) and vector
        # within python interpretor behave the same, see correspond
        return f'<Vector of size {self.shape} {self.values}>'

    def dot(self, value):
        if not isinstance(value, Vector) or self.shape != value.shape:
            raise ValueError("Vectors must have the same dimensions.")
        res = 0
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                res += self.values[i][j] * value.values[i][j]

        return res

    def T(self):
        if self.shape[0] >= self.shape[1]:
            return Vector([[j for i in self.values for j in i]])
        else:
            return Vector([[j] for i in self.values for j in i])
