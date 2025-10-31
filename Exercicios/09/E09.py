def read():
    D = int(input())  
    N = int(input())  
    values = list(map(int, input().split()))
    return D, N, values


def solve(D, N, values):
    # dp[i][estado] → melhor número de diamantes após o dia i
    # estado 0 = livre, 1 = tem passe, 2 = descansando
    dp = [[-float('inf')] * 3 for _ in range(N + 1)]
    dp[0][0] = D  # começa livre, com D diamantes

    for i in range(N):
        # estado 0 (livre)
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][0], dp[i][2])

        # estado 1 (tem passe)
        dp[i + 1][1] = max( dp[i + 1][1], dp[i][1], dp[i][0] - values[i])

        # estado 2 (descansando)
        dp[i + 1][2] = max(dp[i + 1][2], dp[i][1] + values[i])

    return int(max(dp[N]))



X = int(input())
for _ in range(X):
    D, N, values = read()
    print(solve(D, N, values))
