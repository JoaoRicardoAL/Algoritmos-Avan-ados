import math 
def isPrime(x):
    if x < 2 or x % 2 == 0:
        return False
    if x == 2 or x == 3:
        return True 
    top = int(math.sqrt(x)) + 1
    for i in range(3, top, 2):
        if x % i == 0:
            return False
    return True

def solve(n, t):
    p = n + 1 
    while(True):
        if isPrime(p):
            break;
        p += 1
    return pow(t, p-2, p)
    


n, t = input().split()
print(solve(int(n),  int(t)))