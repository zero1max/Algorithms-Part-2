# Task 5

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print(True)
else:
    print(False)