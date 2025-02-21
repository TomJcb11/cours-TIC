class InvalidParameterError(Exception):
    def __init__(self, parameter, options: tuple):
        self.message = f"Only {', '.join(options)} are valid options, '{parameter}' was passed"
        super().__init__(self.message)


class DimensionError(Exception):
    def __init__(self, ndim: int):
        self.message = f'Must be a 2 dimensional array, found {ndim}'
        super().__init__(self.message)


class ShapeMissmatch(Exception):
    def __init__(self, i: int, j: int):
        self.message = f'Found {self.i} features during training but found {self.j} during transform'
        super().__init__(self.message)


class NotFitted(Exception):
    def __init__(self):
        self.message = 'Estimator is not fitted yet'
        super().__init__(self.message)
