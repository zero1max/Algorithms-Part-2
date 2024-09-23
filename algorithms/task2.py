# Task 2

a = int(input("a: "))
b = int(input('b: '))

if a > b:
    natija = a // b 
    qoldiq = a % b   
else:
    natija = b // a 
    qoldiq = b % a   

print(f"Natija: {natija}")
print(f"Qoldiq: {qoldiq}")