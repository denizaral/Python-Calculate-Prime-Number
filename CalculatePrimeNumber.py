// Calculate Prime Number Example

number = int(input("Enter number : "))
primeNumber = True
for x in range(2,number):
    if (number % x) == 0:
        primeNumber = False
        break

if primeNumber:
    print("PRIME")
else:
    print("NOT PRIME")