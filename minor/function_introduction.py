def factorial(n):
    val=1
    for a in range(1,n+1):
        val = val*a
    return val

print('Welcome!')
n = int(input('Enter your number for finding its factorial: '))

print(factorial(n))