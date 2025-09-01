months = int(input())

for _ in range(months):
    days = int(input())
    values = []
    total = 0
    for _ in range(days):
        date, value = input().split()
        values.append((float(value), date))
        total += float(value)
    values.sort(key=lambda x: x[0], reverse=True)
    current_total = 0
    current_days = []
    while current_total <= total / 2:
        current_total += values[0][0]
        current_days.append(values.pop(0))
    current_days.sort(key=lambda x: x[1][6:] + x[1][3:5] + x[1][:2])
    print(f"{len(current_days)} {'dia' if len(current_days) == 1 else 'dias'} ({', '.join([day[1] for day in current_days])}) | soma={current_total:.2f} | {len(current_days) / days * 100:.2f}% dos dias totais")
