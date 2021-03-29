from random import randint

# sets random values for chocalate bar size
N = randint(1, 10000)
M = randint(1, 10000)

# By breaking off a piece we make another piece. 
def split_chocolate(n, m, count=0):
    # so it will take m x n -1 steps to make a 1 x 1 chocolate bar
    return m * n - 1

print(N)
print(M)
print(split_chocolate(N, M))
