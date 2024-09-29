# Task 1

# a = int(input('a: '))

# if a%2 != 0:
#     print('Weird')
# else:
#     print('Not Weird')

# Task 2

# a = int(input('a: '))

# if a%2 == 0 and 2<= a <= 5:
#     print('Not Weird')
# else:
#     print('Weird')

# Task 3

# a = int(input('a: '))

# if a%2 == 0 and 5<= a <= 20:
#     print('Weird')
# else:
#     print('Not Weird')

# Task 4

# a = int(input('a: '))

# if a%2 == 0 and a>= 20:
#     print('Not Weird')
# else:
#     print('Weird')

#------------------------------OR---------------------------

n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
