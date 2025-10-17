"""
Autor: [João Ricardo de Almeida Lustosa]
Esse código faz uso de dois algoritmos para a resolução de problemas de caminho mínimo(Guloso) e par de pontos mais próximos(Divisão e Conquista). 
"""

import math

class UnionFind:
    """
    Representa uma estrutura de dados de Conjuntos Disjuntos (DSU),

    Essa estrutura permite gerenciar conjunto disjuntos a partir de operações de :
        - união de conjuntos (union)
        - busca de elemento (find)

    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        """
        Encontra o representante do conjunto a qual i faz parte, através de path compression.

        Args:
            i (int): elemento a ser buscado
        
        Returns:
            self.parent[i] (int): representante do conjunto de i
        """
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        """
        Faz a união de dois conjuntos que contêm i e j, se i != j.
        utiliza a união por rank, em que o conjunto com menor rank é anexado com o de mair rank.

        Args:
            i, j (int): elementos cujos conjuntos serão unidos

        Returns:
            bool: True se a união foi feita(Os conjuntos eram disjuntos) e False caso contrário.
        """
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
    
        

def dist(a, b):
    """
    Calcula a distancia euclidiana entre dois pontos no R²

    Args:
        a, b: Pontos no espaço
    
    Returns:
        O valor numérico da distância
    """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def read ():
    """
    Lê as entradas necessárias para a resolução do problema

    Args:
        void
    
    Returns:
        n_sys_total: número total de sistemas
        n_sys_important: número de sistemas importantes
        max_tension: tensão máxima subespacial que permite existencia de tunel
        all_systems: lista de todos os sistemas
        imp_systems: lista dos sistemas importantes
        
    """
    all_systems = []
    imp_systems = []
    n_sys_total, n_sys_important, max_tension = input().rstrip().split()
    for i in range(int(n_sys_total)):
        name, x, y = input().rstrip().split()
        coord = (float(x), float(y))
        sys_data = {
            'id' : i,
            'name': name,
            'coord': coord
        }
        all_systems.append(sys_data)
        if i < int(n_sys_important):
            imp_systems.append(sys_data)
    return int(n_sys_total), int(n_sys_important), float(max_tension), all_systems, imp_systems

def greedy (imp_systems, max_tension):
    """
    Algoritmo guloso para encontrar o túnel com menor tensão
    
    Args:
        imp_systems: lista dos sistemas importantes
        max_tension: tensão máxima do tunel
    
    Returns:
        tunels: lista de pares de sistemas que formam o tunel
    """
    if not imp_systems:
        return []
    
    edges = []
    n_important = len(imp_systems)

    for i in range(n_important):
        for j in range(i+1, n_important):
            sys1 = imp_systems[i]
            sys2 = imp_systems[j]

            tension = dist(sys1['coord'], sys2['coord'])
            if tension <= max_tension:
                edges.append((tension, sys1['id'], sys2['id'], sys1['name'], sys2['name']))
    edges.sort(key=lambda x: x[0])

    id_map = {sys['id'] : i for i, sys in enumerate(imp_systems)}

    uf = UnionFind(n_important)
    tunels = []
    edges_count = 0

    for tension, id_1, id_2, name_1, name_2 in edges:
        local_id1 = id_map[id_1]
        local_id2 = id_map[id_2]
    
        if uf.union(local_id1, local_id2):
            tunels.append((name_1, name_2, tension) if id_1 < id_2 else (name_2, name_1, tension))
            edges_count += 1
        if edges_count == n_important - 1:
            break
    return tunels     
        
def div_and_conquer(all_systems):
    """
    Função de chamada do algoritmo de divisão e conquista

    Args:
        all_systems: lista de todos os sistemas
    
    Returns:
        menor ditancia entre dois pontos e o par de sistemas referente a essa distancia

    """
    x_sorted = sorted(all_systems, key=lambda x: x['coord'][0])
    y_sorted = sorted(all_systems, key=lambda y: y['coord'][1])

    return least_dist(x_sorted, y_sorted)

def least_dist(x_sorted, y_sorted):
    """
    Função principal do algoritmo, a qual encontra o par de menor distancia no espaço amostral

    Args: 
        x_sorted: lista dos sistemas ordenados pela coordenada x
        y_sorted: lista dos sistemas ordenados pela coordenada y

    Returns:
        min_band: menor valor de tensão(menor distancia)
        closest_pair: par de menor tensão(distancia)
    """
    n = len(x_sorted)

    if n <= 3:
        return bf(x_sorted)
    
    mid = n // 2
    middle_sys = x_sorted[mid]

    left_x = x_sorted[:mid]
    right_x = x_sorted[mid:]

    left_y, right_y = [], []
    for s in y_sorted:
        if s['coord'][0] <= middle_sys['coord'][0]:
            left_y.append(s)
        else:
            right_y.append(s)

    tension_left, pair_left = least_dist(left_x, left_y)
    tension_right, pair_right = least_dist(right_x, right_y)

    if tension_left < tension_right:
        t, closest_pair = tension_left, pair_left
    else:
        t, closest_pair = tension_right, pair_right

    band = [s for s in y_sorted if abs(s['coord'][0] - middle_sys['coord'][0]) < t]

    min_band = t
    for i in range(len(band)):
        for j in range(i + 1, min(i + 7, len(band))):
            if dist(band[i]['coord'], band[j]['coord']) <= min_band:
                min_band = dist(band[i]['coord'], band[j]['coord'])
                closest_pair = (band[i], band[j])
    return min_band, closest_pair

def bf (systems):
    """
    Função auxiliar para o caso base:

    Args: 
        systems: lista de sistemas
    
    Returns:
        lower: menor valor de tensão(menor distancia)
        closest_pair: par de menor tensão(distancia)
    """
    lower = float('inf')
    closest_pair = None
    n = len(systems)
    for i in range(n):
        for j in range(i+1, n):
            sys1 = systems[i]
            sys2 = systems[j]
            tension = dist(sys1['coord'], sys2['coord'])
            if tension <= lower:
                lower = tension
                closest_pair = (sys1, sys2)

    return lower, closest_pair

# Chamada das Funções e Formatação das saídas
n = int(input()) # Número de casos
for _ in range(n):
    n_sys_total, n_sys_important, max_tension, all_systems, imp_systems = read()
    tunels = greedy(imp_systems, max_tension)
    tension_res, pair = div_and_conquer(all_systems)
    for name_1, name_2, tension in tunels:
        print(f"{name_1}, {name_2}, {tension:.2f}")
    s_pair = sorted(pair, key=lambda p: p['id'])
    print(f"Ponto de Ressonância: {s_pair[0]['name']}, {s_pair[1]['name']}, {tension_res:.2f}")
    print()
