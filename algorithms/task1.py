# Task 1

N = int(input('N: '))

if N%5 == 0 and N%3 == 0:
    print("FizzBuzz")
elif N%3 == 0:
    print("Fizz")
elif N%5 == 0:
    print("Buzz")