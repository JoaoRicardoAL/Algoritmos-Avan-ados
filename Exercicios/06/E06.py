def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(stones):
    stones = sorted(set(stones), key=lambda x: (x[0], x[1]))
    if len(stones) <= 2:
        return stones

    lower = []
    for p in stones:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(stones):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]
    seen = set()
    final_hull = []
    for p in hull:
        if p not in seen:
            final_hull.append(p)
            seen.add(p)
    return final_hull

def solve(case_id):
    N = int(input())
    stones = []
    for _ in range(N):
        e_i, v_i = input().split()
        stones.append((float(e_i), float(v_i)))

    hull = convex_hull(stones)

    print(f"Caso {case_id}:")
    print(f"Tamanho do colar: {len(hull)}")
    print("Pedras ancestrais:", ",".join(f"({e:.4f},{v:.4f})" for e, v in hull))
    print()

if __name__ == "__main__":
    num_cases = int(input())
    for i in range(1, num_cases + 1):
        solve(i)
