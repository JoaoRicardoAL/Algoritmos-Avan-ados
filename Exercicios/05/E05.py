def count_overtakes(arr):
    if len(arr) <= 1:
        return 0, arr
    
    mid = len(arr) // 2
    l_count, l_arr = count_overtakes(arr[:mid])
    r_count, r_arr = count_overtakes(arr[mid:]) 

    m_arr = []
    overtakes = l_count + r_count

    i, j = 0, 0
    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i][1] <= r_arr[j][1]:
            m_arr.append(l_arr[i])
            i += 1
        else:
            m_arr.append(r_arr[j])
            overtakes += len(l_arr) - i
            j += 1
    m_arr.extend(l_arr[i:])
    m_arr.extend(r_arr[j:])

    return overtakes, m_arr

def solve():
    results = []
    N = int(input()) # numbers of sections
    for i in range(N):
        J = int(input()) # numbers of players per section
        players = []
        for _ in range(1, J+1):
            s_0, s_f = input().split()
            pos = (int(s_0), int(s_f))
            players.append(pos)

        players.sort(key=lambda x: x[0]) 
        overtakes, _ = count_overtakes(players)
        results.append((overtakes, i))
    results.sort(key=lambda x: x[0], reverse=True)
    for ot, og_i in results:
        print(f"{og_i} {ot}")

solve()


    

