class PxlVector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return PxlVector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return PxlVector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "PxlVector(x={0}, y={1})".format(self.x, self.y)
