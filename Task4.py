import math
Energetic_state_num = int(input())
first_part = (Energetic_state_num ** 2 * 6.62607015e-34 ** 2 * 8.85418782e-12)
second_part = (math.pi * 9.1093837015e-31 * 1.602176634e-19)
orbit_radius = first_part/second_part
print(float('{:.4e}'.format(orbit_radius)))
  