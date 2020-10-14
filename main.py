class Pascal:

    def __init__(self, list):
        self.list = list

    def __getitem__(self, key):
        return self.list[key - 1]

    def __setitem__(self, key, value):
        self.list[int(key) - 1] = value

    def __str__(self):
        return str(self.list)


a  = Pascal([1,2,3])
print(a)
