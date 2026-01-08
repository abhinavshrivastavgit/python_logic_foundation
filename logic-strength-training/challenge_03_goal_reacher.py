# challenge_03_goal_reacher.py
import random


goal = 30000
saved = []
total_saved = 0
total_saved_month=0

range_loop = random.randint(28,31)
for i in range(0, range_loop):
    saved_today = random.randint(100,5000)
    saved.append(saved_today)
    total_saved_month=total_saved_month+saved_today


print(f'your saving across the month is: {saved}')

print(f'You saved {total_saved_month} rupees for this month.')

day = 0
for saves in saved:
    if total_saved >=30000:
        print(f'you save: {total_saved} in {day} day')
        break
    else:
        total_saved =total_saved+saves
        day = day+1

    