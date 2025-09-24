import sys
from collections import deque

PROD = {
    "Aprendiz": 0.75,
    "Aventureiro": 1.0,
    "Cavaleiro": 1.2,
    "Mestre": 1.5,
    "Lenda": 2.0
}

def solve():
    data = sys.stdin.read().strip().splitlines()
    t = int(data[0])
    idx = 1

    for case in range(t):
        n, m = map(int, data[idx].split()); idx += 1

        heroes = []
        for i in range(n):
            nome, nivel = data[idx].split(); idx += 1
            heroes.append({'id': i, 'nome': nome, 'prod': PROD[nivel], 'free': 0.0, 'quests': []})

        base_time = [0]*(m+1)
        prereq = [[] for _ in range(m+1)]
        dependents = [[] for _ in range(m+1)]
        in_deg = [0]*(m+1)

        for _ in range(m):
            parts = list(map(int, data[idx].split())); idx += 1
            qid = parts[0]
            base_time[qid] = parts[1]
            if parts[2] == 0:
                deps = []
            else:
                deps = parts[2:]
            prereq[qid] = deps
            in_deg[qid] = len(deps)
            for d in deps:
                dependents[d].append(qid)

        finish_time = [0.0]*(m+1)
        ready = deque()
        for q in range(1, m+1):
            if in_deg[q] == 0:
                ready.append(q)

        done = 0
        while ready:
            q = ready.popleft()
            start_dep = max((finish_time[d] for d in prereq[q]), default=0.0)

            best_h = None
            best_finish = float('inf')
            for hi, hero in enumerate(heroes):
                start = max(hero['free'], start_dep)
                exec_time = base_time[q] / hero['prod']
                finish = start + exec_time
                if best_h is None or finish < best_finish - 1e-9 or (abs(finish - best_finish) < 1e-9 and hi < best_h):
                    best_h = hi
                    best_finish = finish

            hero = heroes[best_h]
            hero['free'] = best_finish
            hero['quests'].append(q)
            finish_time[q] = best_finish
            done += 1

            for dep in dependents[q]:
                in_deg[dep] -= 1
                if in_deg[dep] == 0:
                    ready.append(dep)

        total_time = max(finish_time)
        for hero in heroes:
            quests_str = ",".join(str(q) for q in hero['quests'])
            print(f"{hero['nome']} = {{{quests_str}}}")
        print(f"Tempo mínimo: {total_time:.2f}")
        if case != t - 1:
            print()

if __name__ == "__main__":
    solve()
