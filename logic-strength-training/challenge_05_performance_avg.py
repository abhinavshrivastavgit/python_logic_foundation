#challenge_05_performance_avg.py

score = [85, 90, 78, 92, 100]
total_score=0

for i in range(0,len(score)):
    total_score = total_score + int(score[i])

avg = total_score/len(score)
print(f'your average for the solution is: {avg}')