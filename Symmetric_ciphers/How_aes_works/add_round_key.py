state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    result = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = state[i][j] ^ round_key[i][j]
    return result

result = add_round_key(state,round_key)

def matrix2bytes(matrix):
    return bytes([matrix[i][j] for i in range(4) for j in range(4)])

print(matrix2bytes(result))

## initialize state and round keys
# adding the round key function
# convert the matrix to bytes
# print bytes of the conversion