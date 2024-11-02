# This is modified code of 16 diagonals to find maximum number of such
# diagonals possible for a n by n matrix
# although its extremely slow for n > 5 but still works
# 0 represents no diagonal placed
# 1 represents diagonal placed as '/'
# 2 represents diagonal placed as '\'

maximum = current = 0
n = 5

def is_extendable(perm, i, j):
    if perm[i][j] == 1:
        if i > 0 and (j < n-1 and perm[i-1][j+1] == 1 or perm[i-1][j] == 2):
            return False
        if j > 0 and perm[i][j-1] == 2:
            return False

    if perm[i][j] == 2:
        if i > 0 and (j > 0 and perm[i-1][j-1] == 2 or perm[i-1][j] == 1):
            return False
        if j > 0 and perm[i][j-1] == 1:
            return False

    return True

def extend(perm, i, j):
    global current, maximum
    if j == n:
        i+=1
        j=0
    if i == n:
        maximum = max(current, maximum)
        return

    if maximum - current > n*n -(i*n +j):
        return

    for k in range(3):
        perm[i][j] = k
        if k != 0:
            current+=1
        if is_extendable(perm, i, j):
            extend(perm, i, j+1)
        if k != 0:
            current-=1

extend([[0 for i in range(n)] for j in range(n)], 0, 0)
print(maximum)