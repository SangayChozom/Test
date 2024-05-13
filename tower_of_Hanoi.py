
def toh(N, fromm, to, aux):
    if N == 1:
        print("move disk", N, "from rod", fromm, "to rod", to)
        return 1
    moves = 0
    moves += toh(N-1, fromm, aux, to)
    print("move disk", N, "from rod", fromm, "to rod", to)
    moves += 1
    moves += toh(N-1, aux, to, fromm)
    return moves

n = int(input ("Enter the number of disk: "))
print(toh(n, 1, 3, 2))