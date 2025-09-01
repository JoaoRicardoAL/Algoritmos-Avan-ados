example = [1, 0, 1, 0, 1]

def light(bulbs):
    cost = 0
    for i in range(len(bulbs)):
        b = bulbs[i] if cost % 2 == 0 else not bulbs[i]
        if not b:
            cost += 1
    return cost

print(light(example))