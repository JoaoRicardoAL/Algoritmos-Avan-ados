X = int(input())

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        r_i = self.find(i)
        r_j = self.find(j)

        if r_i != r_j:
            if self.rank[r_i] < self.rank[r_j]:
                self.parent[r_i] = r_j
            elif self.rank[r_i] > self.rank[r_j]:
                self.parent[r_j] = r_i
            else:
                self.parent[r_j] = r_i
                self.rank[r_i] += 1
            return True
        return False
    
def read():
    int_line = input().strip().split()
    N = int(int_line[0]) # num de acampamentos
    M = int(int_line[1]) # num de pontes possiveis de reconstrução

    edges = []
    cost_seen = []
    is_valid = True
    for i in range(M):
        edge_line = input().strip().split()
        u = int(edge_line[0])
        v = int(edge_line[1])
        c = int(edge_line[2])

        if c in cost_seen:
            is_valid = False
        else:
            cost_seen.append(c)
            edges.append((c, u, v)) # (custo, u, v)
    edges.sort() # Ordena pelo menor custo para realizar kruskal
    if is_valid:
        return N, M, edges
    else:
        return N, M, []

def solve(N,M, edges):  
    # Algoritmo Kruskal
    dsu = DSU(N+1)
    custo = 0
    cont = 0
    res = []
    for c, u, v in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            custo += c
            res.append((u, v))
            cont += 1
            if cont == N - 1:
                break
    return custo, res

for i in range(X):
    N, M, edges = read()
    if edges:
        custo, pontes = solve(N, M, edges)
        if len(pontes) < N-1:
                print("O vale nao pode ser completamente atravessado.\n")

        else:     
            print(f"Custo minimo: {custo}")
            print("Pontes reconstruidas:")
            for u, v in pontes:
                pontos = sorted([u, v]) 
                print(f"{pontos[0]} - {pontos[1]}")
            print()
    else:
        print("Esse nao e o caminho correto para a Cidade Perdida de Z.\n")
    


