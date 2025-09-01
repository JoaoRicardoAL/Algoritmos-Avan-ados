numbers = [-1, -5, -3, 4, 2, 1]

numbers.sort(key=lambda x: -x)
biggest = numbers[0] * numbers[1] * numbers[2]
_2smallest1biggest = numbers[0] * numbers[-1] * numbers[-2]

print(max(biggest, _2smallest1biggest))