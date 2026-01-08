#"challenge_01_Thermal_throttler.py"

import random

gpu_temps = []

temp_count = int(input('Enter the number of interval you want result for: '))

for i in range(0, temp_count):
    temp_value = random.randint(50,95)
    gpu_temps.append(temp_value)

for temp in gpu_temps:
    if temp >80:
        print(f'Slow Down your CPU temp is: {temp}')
    else:
        print(f'Keep running your CPU temp is:{temp}')
