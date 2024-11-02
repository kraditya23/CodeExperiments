# This is the code to find the placement of diagonals in the question
# "Place 16 diagonals in a 5 by 5 matrix such that no two diagonals touch each other"
# 0 represents no diagonal placed
# 1 represents diagonal placed as '/'
# 2 represents diagonal placed as '\'


count = 0

def is_extendable(perm, i, j):
    if perm[i][j] == 1:
        if i > 0 and (j < 4 and perm[i-1][j+1] == 1 or perm[i-1][j] == 2):
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
    global count
    if j == 5:
        i+=1
        j=0
    if i == 5:
        if count == 16:
            print(perm)
        return

    if (16 - count) > (25 - (i*5 + j)):
        return
    # this checks if the remaining boxes are less than the number of diagonals
    # to be placed, if yes, there is no point in checking further
    # this extra check might seem like a small change in the code
    # but it makes a significant effect on time
    # it takes around 29s to find the two possible results without this check
    # but takes merely 0.19s with this check in place

    for k in range(3):
        perm[i][j] = k
        if k != 0:
            count+=1
        if is_extendable(perm, i, j):
            extend(perm, i, j+1)
        if k != 0:
            count-=1

extend([[0 for i in range(5)] for j in range(5)], 0, 0)