#challenge_02_Odd_Only_filter.py

import random
odd_ids = [] #this will act as our result bracket

list_lenght = random.randint(5,20) #lenght of the list byu random

data_list = [] #data list

for i in range(0,list_lenght):
    value = random.randint(0,1000)
    data_list.append(value)

for data in data_list:
    if data%2==1:
        odd_ids.append(data)
    else:
        continue

print(f'Lenght choosen by the system: {list_lenght}')
print(f'Your data list is: {data_list}')

odd_ids.sort() #sorting the odd_id list
print(f'Your Odd sorted list is: {odd_ids}')
