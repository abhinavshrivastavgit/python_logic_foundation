scores = [70,85,99,92,99,88]
lenght = len(scores)

max_score =  scores[0]
for i in range(0,lenght):
    if scores[i]>max_score:
      max_score = scores[i]
    
others =[]
for i in range(0, lenght):
   if scores[i]!=max_score:
      others.append(scores[i])


max_others = others[0]
lenght1= len(others)
for i in range(0, lenght1):
   if others[i]>max_others:
      max_others=others[i]
print(f'Runner-Up: {max_others}')
# if len(others)>0:
#    runner_up = max(others)
#    print(f'Runner-Up: {runner_up}')
# else:
#    print('No Runner-up')