import numpy as np

def extractPosition(i, positions):
    positionsAsBinary = sum([1 << position for position in positions])
    relevantBits = i & positionsAsBinary
    result = sum([((relevantBits >> position) & 1) << i for i, position in enumerate(positions)])
    return result

def expand(operator, nQbits, positions):
    nStates = 2**nQbits
    result = np.zeros([nStates, nStates])
    positionsAsBinary = sum([1 << position for position in positions])
    for i in range(nStates):
        iPos = extractPosition(i, positions)
        for j in range(nStates):
            jPos = extractPosition(j, positions)
            if (~positionsAsBinary & i) == (~positionsAsBinary & j):
                result[i][j] = operator[iPos, jPos]
    return result



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

print(expand(swap, 3, [0, 2]))
