import numpy as np

image = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

kernel = np.array([[1,0],
                   [0,1]])

n = image.shape[0]
f = kernel.shape[0]

conv_output = []
for i in range(n - f + 1):
    row = []
    for j in range(n - f + 1):
        s = 0
        for x in range(f):
            for y in range(f):
                s += image[i+x][j+y] * kernel[x][y]
        row.append(s)
    conv_output.append(row)

conv_output = np.array(conv_output)
print("Convolution Output:")
print(conv_output)

p = conv_output.shape[0]
pool_size = 2

pool_output = []
for i in range(0, p, pool_size):
    row = []
    for j in range(0, p, pool_size):
        m = conv_output[i][j]
        for x in range(pool_size):
            for y in range(pool_size):
                if conv_output[i+x][j+y] > m:
                    m = conv_output[i+x][j+y]
        row.append(m)
    pool_output.append(row)

pool_output = np.array(pool_output)
print("Max Pooling Output:")
print(pool_output)

flatten = []
for i in range(len(pool_output)):
    for j in range(len(pool_output[0])):
        flatten.append(pool_output[i][j])

print("Flatten Output:")
print(flatten)