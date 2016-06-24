
class Iterator(object):
    def __init__(self, list_iterable):
        # self.l = list_iterable
        self.iterators = map(lambda x: iter(x), list_iterable)
        self.current_i = iter(self.iterators)
        self.length = len(list_iterable)
        self.deleted = 0

    def __iter__(self):
        return self

    def next(self):
        try:
            i = self.current_i.next()
        except StopIteration:
            self.current_i = self.iterators.__iter__()
            i = self.current_i.next()
        try:
            res = i.next()
            return res
        except StopIteration:
            self.deleted += 1
            if self.deleted == self.length:
                raise StopIteration
            return self.next()

a = ["a1", "a2"]
b = ["b1"]
c = ["c1", "c2", "c3"]

for x in Iterator([a, b, c]):
    print x

# iter(a)
# iter(b)
# iter(c)


# for i in izip_longest(iter(a), iter(b), iter(c)):
#     print i



