X = int(input())


def solve(s):
    if not s:
        return ""
    n = len(s)
    if n == 0:
        return ""
    
    lps = [0]*n
    length = 0
    i = 1

    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    tam = lps[-1]
    return s[:tam]
        
    
for _ in range(X):
    s = input().strip()
    print(solve(s))