#grade checking function
def grading_func(score):
    if score>=90:
        return "Grade A"
    elif score>=70 and score<90:
        return "Grade B"
    else:
        return "Need Improvement"
    
#taking input from the user
score = int(input('Enter the score: '))

print(f'You scored:{score} and secured {grading_func(score)}')