from collections import deque

def read():
    int_line = input().strip().split()
    n = int(int_line[0])
    m = int(int_line[1])

    edges = []
    for i in range(m):
        edge_line = input().strip().split()
        a = int(edge_line[0])
        b = int(edge_line[1])
        c = int(edge_line[2])
        edges.append((a, b, c))
    
    return n, m, edges


def max_flow(n, cap, G, s, t):
    flow = 0
    while True:
        parent = [-1] * (n + 1)
        parent[s] = s
        Q = deque([s])

        # BFS
        while Q and parent[t] == -1:
            u = Q.popleft()
            for v in G[u]:
                if parent[v] == -1 and cap[u][v] > 0:
                    parent[v] = u
                    Q.append(v)

        if parent[t] == -1:
            break

        # gargalo
        v = t
        gargalo = float('inf')
        while v != s:
            u = parent[v]
            gargalo = min(gargalo, cap[u][v])
            v = u

        # atualiza capacidades
        v = t
        while v != s:
            u = parent[v]
            cap[u][v] -= gargalo
            cap[v][u] += gargalo
            v = u
        
        flow += gargalo

    return flow


def solve(n, m, edges):
    cap = [[0]*(n + 1) for _ in range(n + 1)]
    G = [[] for _ in range(n + 1)]

    for a, b, c in edges:
        if cap[a][b] == 0:
            G[a].append(b)
            G[b].append(a)
        cap[a][b] += c

    print(max_flow(n, cap, G, 1, n))


n, m, edges = read()
solve(n, m, edges)
