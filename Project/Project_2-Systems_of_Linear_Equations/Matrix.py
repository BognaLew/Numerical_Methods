import pandas

from constants import ZERO


class Matrix:
    def __init__(self, N, a1, a2, a3):
        self.N = N
        self.M = []
        for i in range(ZERO, N):
            row = []
            for j in range(ZERO, i - 2):
                row.append(ZERO)
            if i > 1:
                row.append(a3)
            if i > 0:
                row.append(a2)
            row.append(a1)
            if i < N - 1:
                row.append(a2)
            if i < N - 2:
                row.append(a3)
            for j in range(len(row), N):
                row.append(ZERO)
            self.M.append(row)

    def oneRowMul(self, row, v):
        s = ZERO
        for c in range(ZERO, self.N):
            s += self.M[row][c] * v.b[c]
        return s

    def __mul__(self, v):
        u = []
        for r in range(ZERO, self.N):
            u.append(self.oneRowMul(r, v))
        return u

    def __add__(self, matrix):
        newM = Matrix(self.N, ZERO, ZERO, ZERO)
        for r in range(ZERO, self.N):
            for c in range(ZERO, self.N):
                newM.M[r][c] = self.M[r][c] + matrix.M[r][c]
        return newM

    def getDiagonal(self):
        D = Matrix(self.N, ZERO, ZERO, ZERO)
        for r in range(ZERO, self.N):
            for c in range(ZERO, self.N):
                if c == r:
                    D.M[r][c] = self.M[r][c]
                else:
                    D.M[r][c] = ZERO
        return D

    def getUp(self):
        U = Matrix(self.N, ZERO, ZERO, ZERO)
        for r in range(ZERO, self.N):
            for c in range(ZERO, r + 1):
                U.M[r][c] = ZERO
            for c in range(r + 1, self.N):
                U.M[r][c] = self.M[r][c]
        return U

    def getLow(self):
        L = Matrix(self.N, ZERO, ZERO, ZERO)
        for r in range(0, self.N):
            for c in range(ZERO, r):
                L.M[r][c] = self.M[r][c]
            for c in range(r, self.N):
                L.M[r][c] = ZERO
        return L
