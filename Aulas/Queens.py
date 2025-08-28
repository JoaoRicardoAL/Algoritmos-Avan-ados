x, y = input().rstrip().split(' ')
x = int(x)
y = int(y)

def check_diagonal(queens, r, i):
    for r_a, i_a in enumerate(queens):
        if i_a == -1:
            continue
        if (abs(r_a - r) == abs(i_a - i)):
            return False
    return True

def place_queens(queens):
    if not -1 in queens:
        return queens
    
    for r in queens:
        if queens[r] != -1:
            continue
        for i in range(8):
            if i in queens:
                continue
            if not check_diagonal(queens, r, i):
                continue
            n_queens = queens.copy()
            n_queens[r] = i
            res = place_queens(n_queens)
            if res:
                return res
    return []
        
queens = [-1] * 8
queens[x] = y
res = place_queens(queens)
print(res)