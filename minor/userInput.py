# User Input basic interface Program
name = input('Enter your name: ')
print('Hello',name, '!')

#User Program to make decision which program he/she wants to run
opt=input('Do you want to run other program: ')

if opt.lower() == "yes":
 print('Here is the list of program:\n1. Gross Pay calculator. \n2. Calculator. \n3. Exit.\n ')
 innerOpt = int(input('Select an option: '))
 if innerOpt ==1:
  #Exercise2 a program to prompt the user for hours and ratre per hour to compute gross pay
  hours = float(input('Enter Hours:'))
  rate = float(input('Enter Rate:'))
  pay = hours*rate
  print('Total pay amount is:',pay)
  #Arithmetic Operation
 elif innerOpt == 2:
  num1= int(input('Enter First Number:'))
  num2= int(input('Enter Second Number:'))
  print('Sum is:',num1+num2)
  print('Subtract is:',num1-num2)
  print('Multiplication is:',num1*num2)
  # Added a check to prevent division by zero error
  if num2 != 0:
            print('Division is:', num1 / num2)
  else:
            print('Cannot divide by zero.')
 #Exit
 elif innerOpt ==3:
  print('Thank you',name,'for your precious time.')
  quit()
 
else:
 print('Thank you',name,'for your precious time.')
 



