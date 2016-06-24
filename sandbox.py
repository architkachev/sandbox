class Iterator(object):
    def __init__(self, iterable):
        self.iterator = iter(filter(lambda x: x > 0, iterable))
        self.buf = next(self.iterator, None)

    def __iter__(self):
        return self

    def next(self):
        if self.buf is not None:
            # a = self.buf
            # self.buf = next(self.iterator, None)
            # return a
            a, self.buf = self.buf, next(self.iterator, None)
            return a
        else:
            raise StopIteration

    def has_next(self):
        return True if self.buf is not None else False


for i in Iterator([1, 2, -2, -5, 3]):
    print i