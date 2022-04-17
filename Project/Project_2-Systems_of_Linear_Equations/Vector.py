from math import sin, sqrt


class Vector:

    def __init__(self, N, f):
        self.N = N
        self.b = []
        for n in range(1, N+1):
            self.b.append(sin(n*(f+1)))

    def calculateResiduum(self, A, b):
        r = []
        s = A.__mul__(self)
        for i in range(0, self.N):
            r.append(s[i] - b.b[i])
        return r

    def calculateNorm(self, A, b):
        residuum = self.calculateResiduum(A, b)
        sum = 0
        for e in residuum:
            sum += e ** 2
        return sqrt(sum)
