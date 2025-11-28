X = int(input())

def read():
    line = input().strip().split()
    n = int(line[0])
    m = int(line[1])
    s = int(line[2])

    adj = [[] for _ in range(n)]
    for i in range(m):
        edge = input().strip().split()
        u = int(edge[0])
        v = int(edge[1])
        adj[u].append(v)
    
    return n, m, s, adj

def solve(n, m, s, adj):
    memo = [-1] * n

    def tem_estrategia_vencedora(u):
        if memo[u] != -1:
            return memo[u]
        
        can_force_loss = False
        for v in adj[u]:
            if not tem_estrategia_vencedora(v):
                can_force_loss = True
                break
        if can_force_loss:
            memo[u] = 1
            return True
        else:
            memo[u] = 0
            return False
    
    if tem_estrategia_vencedora(s):
        print("Ash")
    else:
        print("Noir")

for _ in range(X):
    n, m, s, adj = read()
    solve(n, m, s, adj)
