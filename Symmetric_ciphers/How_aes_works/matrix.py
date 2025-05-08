import numpy as np

def bytes2matrix(text):

    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):

    mat = np.matrix(matrix)
    bytes = mat.tobytes()
    return bytes.decode('ascii')

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))

# this function converts matrix to bytes
# and converts bytes to matrix that is needed in AES algo