gaps = [[1, 4], [2, 3], [4, 6], [8, 9]]

def distribute(gaps):
    gaps.sort(key=lambda x: x[1])
    print(gaps)
    count = 1

    selected = []

    for gap in gaps[1:]:
        if gap[0] >= gaps[-1][1]:
            continue

        count += 1
        selected.append(gap)

    return count
print(distribute(gaps))

