class Vector:
    def __init__(self, values) -> None:
        self.shape = 'shape'
        self.values = values
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
