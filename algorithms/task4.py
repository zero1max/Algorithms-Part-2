# Task 4

a = int(input('a: '))

if a%2 == 0 and a%3 == 0 and a%5 == 0:
    print('A')
elif a%2 == 0 and a%3 == 0:
    print('B')
elif a%2 == 0 and a%5 == 0:
    print('C')
elif a%3 == 0 and a%5 == 0:
    print("D")
elif a%2 == 0 or a%3 == 0 or a%5 == 0:
    print('E')
elif a%2 != 0 and a%3 != 0 and a%5 != 0:
    print("N")