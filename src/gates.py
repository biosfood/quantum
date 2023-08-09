import numpy as np
import time

def extractPosition(i, positions, positionsAsBinary):
    relevantBits = i & positionsAsBinary
    result = sum([((relevantBits >> position) & 1) << i for i, position in enumerate(positions)])
    return result

def expand(nQbits, operator, positions):
    nStates = 2**nQbits
    result = np.zeros([nStates, nStates])
    positionsAsBinary = sum([1 << position for position in positions])
    for i in range(nStates):
        iPos = extractPosition(i, positions, positionsAsBinary)
        for j in range(nStates):
            jPos = extractPosition(j, positions, positionsAsBinary)
            if (~positionsAsBinary & i) == (~positionsAsBinary & j):
                result[i][j] = operator[iPos, jPos]
    return result

start = time.time()

swap = np.array([
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
])

Not = np.array([
    [0, 1],
    [1, 0],
])

cnot = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

ccnot = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
])

n = 12 # 8 in, 4 out

steps = [
    expand(n, cnot,  [7, 8]),
    expand(n, ccnot, [6, 8, 9]),
    expand(n, ccnot, [5, 6, 8]),
    expand(n, ccnot, [4, 7, 9]),
    expand(n, cnot,  [3, 10]),
    expand(n, cnot,  [2, 10]),
    expand(n, ccnot, [5, 8, 10]),
    expand(n, ccnot, [4, 10,11]),
    expand(n, ccnot, [1, 3, 11]),
    expand(n, ccnot, [0, 9, 10]),
    expand(n, ccnot, [8, 9, 10]),
    expand(n, ccnot, [0, 4, 11]),
    expand(n, ccnot, [1, 8, 11]),
    expand(n, ccnot, [2, 10,11]),
    expand(n, ccnot, [8, 10,11]),
    expand(n, cnot,  [9, 8]),
]

forward = np.identity(2**n)

print(forward)

for step in steps:
    forward = forward @ step

test = np.random.rand(2**n)

print(forward, test, test @ forward)

end = time.time()

print(f'took {end-start} seconds')
