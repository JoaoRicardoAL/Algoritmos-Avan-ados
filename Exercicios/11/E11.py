X = int(input())

def read():
    int_line = input().strip().split()
    N = int(int_line[0]) # num de vertices
    M = int(int_line[1]) # num de arestas

    # Lista de Adjacencia
    graph = [[] for _ in range(N+1)]

    for i in range(M):
        edge = input().strip().split()
        u = int(edge[0])
        v = int(edge[1])
        graph[u].append(v)
        graph[v].append(u)

    return N, M, graph

def solve(N, M, G):
    # Usar DFS
    visited = [False for _ in range(N+1)]
    counter = 0 # Conta a quantidade de grafos disjuntos na rede 

    def DFS(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS(v)

    for i in range(1, N+1):
        if not visited[i]:
            counter += 1
            DFS(i) 
    
    return counter

for _ in range(X):
    N, M, G = read()
    print(solve(N, M, G))
