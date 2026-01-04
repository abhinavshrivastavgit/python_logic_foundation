#creating user input taking list
scores = []
value_lenght = int(input('Enter how many scores you want to store: '))

#storing scores in the list
for i in range(0,value_lenght):
  score_val = int(input('Enter the score obtained: '))
  scores.append(score_val)

#adding condition and condition checking
for s in scores:
  if s>=90:
    print(f'You had scored: {s}, and secured Grade A')
  elif 89>s>=70:
    print(f'You had scored: {s}, and secured Grade B')
  else:
    print(f'You had scored: {s}, and You need Improvement')

