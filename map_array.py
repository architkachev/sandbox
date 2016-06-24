class ArrayMap(object):
    def __init__(self):
        self.d = {}
        self.l = []

    def append(self, item):
        self.l.append(item)
        self.d[self.l.index(item)] = item

    def __getitem__(self, item):
        return self.l[item]

    def __setitem__(self, key, value):
        pass


a = ArrayMap()


a.append("Artsiom")
a.append(15)
a.append("Sasha")
a.append(12.45)

print 13