import time

from constants import N, epsilon, ZERO
from Vector import Vector

def prepare(A):
    iterations = ZERO
    x = Vector(N, ZERO)
    xPrev = Vector(N, ZERO)
    Norm = 1
    L = A.getLow()
    U = A.getUp()
    LplusU = L.__add__(U)
    for i in range(ZERO, N):
        x.b[i] = 1
        xPrev.b[i] = 1
    return iterations, Norm, xPrev, x, LplusU

def Jacobi(A, b):
    iterations, Norm, xPrev, x, LplusU = prepare(A)
    t0 = time.time()
    while Norm > epsilon:
        tmp = LplusU.__mul__(xPrev)
        for i in range(ZERO, N):
            x.b[i] = (b.b[i] - tmp[i]) / A.M[i][i]
        xPrev = x
        Norm = x.calculateNorm(A, b)
        iterations += 1
    t1 = time.time()
    print("JACOBI METHOD")
    print("iterations: " + str(iterations))
    print("time: " + str(t1-t0))
    print("norm: " + str(Norm))
    return x


def Gauss_Seidel(A, b):
    iterations, Norm, xPrev, x, LplusU = prepare(A)
    t0 = time.time()
    while Norm > epsilon:
        for i in range(ZERO, N):
            tmp = LplusU.oneRowMul(i, xPrev)
            x.b[i] = (b.b[i] - tmp) / A.M[i][i]
            xPrev = x
        Norm = x.calculateNorm(A, b)
        iterations += 1
    t1 = time.time()
    print("GAUSS-SEIDEL METHOD")
    print("iterations: " + str(iterations))
    print("time: " + str(t1-t0))
    print("norm: " + str(Norm))
    return x

