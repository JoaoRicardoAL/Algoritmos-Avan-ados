def read ():
    n = int(input())
    line = input().strip()
    dots = []
    for pair in line.split():
        pair = pair.strip("()")
        x, y = map(int, pair.split(','))
        dots.append(x + y)
    return n, dots

def solve(n, dots):
    dp = [[0] * n for _ in range(n)]
        
   
    pre_sum = [0] * (n+1)
    for i in range(n):
        pre_sum[i+1] = pre_sum[i] + dots[i]

    def get_sum (i, j):
        if i > j:
            return 0
        return pre_sum[j+1] - pre_sum[i]

    for k in range(1, n+1):
        for i in range(n - k + 1):
            j =  i + k - 1
            if k == 1:
                dp[i][j] = dots[i]
            else:
                dp[i][j] = max(dots[i] + (get_sum(i + 1, j) - dp[i + 1][j]),
                               dots[j] + (get_sum(i, j - 1) - dp[i][j - 1]))
    return dp[0][n-1]
x = int(input())
for _ in range(x):
    n, dots = read()
    print(solve(n, dots))


