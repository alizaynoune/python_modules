class Vector:
    def __init__(self, values) -> None:
        self.values = [[]]
        # a list of a list of floats: Vector([[0.0, 1.0, 2.0, 3.0]]),
        # a list of lists of single float: Vector([[0.0], [1.0], [2.0], [3.0]]),
        if isinstance(values, list):
            val_len = len(values)
            if val_len == 1 and not len(values[0]):
                raise ValueError('error is empty')
            for i in values[0] if val_len == 1 else values:
                if val_len != 1:
                    if not isinstance(i, list) or not len(i) == 1 or not isinstance(i[0], float):
                        raise ValueError('error {}'.format(i))
                else:
                    if not isinstance(i, float):
                        raise ValueError('error {}'.format(i))

            self.values = values[:]
            self.shape = (val_len, len(values[0]))
        # Vector(3) -> the vector will have values = [[0.0], [1.0], [2.0]],
        elif isinstance(values, int):
            if values <= 0:
                print('error')
            # [c for c in new_list if len(c) > minLen]
            self.shape = (1, values)
            self.values = [[float(i) for i in range(values)]]
        elif isinstance(values, range):
            if values.start < 0 or values.start >= values.stop:
                raise ValueError('error {}'.format(values))
            self.shape = (1, values.stop - values.start)
            self.values = [[float(i) for i in values]]

        pass

    def __add__(self, value):
        if self.shape[0] >= self.shape[1]:
            self.values = [[j + value] for i in self.values for j in i]
        else:
            self.values = [[j + value for i in self.values for j in i]]
        return self

    def __radd__(self, v):
        return self.__add__(v)
    # add & radd : only vectors of same shape.

    def __sub__(self):
        print('sub done')

    def __rsub__(self):
        print('rsub done')
    # sub & rsub: only vectors of same shape.

    def __truediv__(self, value):
        if value == 0:
            raise ValueError('ZeroDivisionError: division by zero.')
        if self.shape[0] >= self.shape[1]:
            self.values = [[j / value] for i in self.values for j in i]
        else:
            self.values = [[j / value for i in self.values for j in i]]
        return self
    # truediv : only with scalars (to perform division of Vector by a scalar).

    def __rtruediv__(self, value):
        raise ValueError(
            'this test can be commented for the other tests and uncommented to show this one')
    # rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."

    def __mul__(self, value):
        if self.shape[0] >= self.shape[1]:
            self.values = [[j * value] for i in self.values for j in i]
        else:
            self.values = [[j * value for i in self.values for j in i]]

        return self

    def __rmul__(self, v):
        return self.__mul__(v)
    # mul & rmul: only scalars (to perform multiplication of Vector by a scalar).

    def __str__(self):
        return f'Vector({self.values})'

    def __repr__(self):
        print('repr done')
    # must be identical, i.e we expect that print(vector) and vector within python interpretor behave the same, see correspond

    def dot(self, value):
        #  res = 0
        if not isinstance(value, Vector) or self.shape != value.shape:
            raise ValueError("Vectors must have the same dimensions.")
        # for i, val in enumerate(self.values):
        #     if isinstance(val, list):
        #         res += val[0] * v.values[i][0]
        #     else:
        #         res += val * v.values[i]
        # return res
        res = 0
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                res += self.values[i][j] * value.values[i][j]

        return res

    def T(self):
        if self.shape == (1, 1):
            return self
        if self.shape[0] >= self.shape[1]:
            self.values = [[j for i in self.values for j in i]]
        else:
            self.values = [[j] for i in self.values for j in i]
        self.shape = (len(self.values), len(self.values[0]))
        return self
