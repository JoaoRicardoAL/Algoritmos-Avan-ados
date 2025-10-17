def read():
    n = int(input())
    stones = []
    line = input().rstrip().split()
    for i in range(n):
        stone = int(line[i]) 
        stones.append(stone)
    return n, stones

def solve(n, stones):
    s = [0] + stones

    dp = [[0, 0] for _ in range(n + 1)]

    dp[0][0] = 0
    dp[0][1] = 1

    for i in range(1, n + 1):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + s[i]
        
        cost_from_prev_1 = dp[i-1][1] + (s[i] - 1)
        
        cost_from_prev_0 = dp[i-1][0] + max(s[i] - (i - 1), 0)
        
        dp[i][1] = min(cost_from_prev_1, cost_from_prev_0)
        
    return min(dp[n][0], dp[n][1])

n, stones = read()
print(solve(n, stones))