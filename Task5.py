import math
x = float(input())
miu = float(input())
teta = float(input())
first_part = 1 / math.sqrt(2 * math.pi * teta ** 2 )
second_part = math.e ** (- ((x - miu) ** 2) / (2 * teta ** 2))
result = first_part * second_part
print('{:.10}'.format(result))

