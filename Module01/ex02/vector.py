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
            self.shape = (val_len, len(values[0]) if val_len else 0)
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
        print('add done')

    def __radd__(self):
        print('radd done')
    # add & radd : only vectors of same shape.

    def __sub__(self):
        print('sub done')

    def __rsub__(self):
        print('rsub done')
    # sub & rsub: only vectors of same shape.

    def __truediv__(self, value):
        print('truediv done')
    # truediv : only with scalars (to perform division of Vector by a scalar).

    def __rtruediv__(self, value):
        print(self, value)
    # rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."

    def __mul__(self, value):
        # for i in self.v:
        #     print(i)
        return self

    def __rmul__(self):
        print('rmul done')
    # mul & rmul: only scalars (to perform multiplication of Vector by a scalar).

    def __str__(self):
        return f'Vector({self.values})'

    def __repr__(self):
        print('repr done')
    # must be identical, i.e we expect that print(vector) and vector within python interpretor behave the same, see correspond

    def dot(self, value):
        print('dot done')

    def T(self):
        print('T done')
        return self
