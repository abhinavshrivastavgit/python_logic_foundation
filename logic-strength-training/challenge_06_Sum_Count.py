#touch challenge_07_Sum_Count.py
import random

rand_list = []

lenght = random.randint(5,10)
for i in range(0,lenght):
    value = random.randint(1,20)
    rand_list.append(value)

print(rand_list)

sum = 0
for element in rand_list:
    sum = sum + element

print(f'The sum of this random list is: {sum}')