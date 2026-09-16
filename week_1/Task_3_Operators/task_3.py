first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("\n----- Calculator -----")
print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)

if second_number != 0:
    print("Division:", first_number / second_number)
    print("Modulus:", first_number % second_number)
else:
    print("Division: Cannot divide by zero")
    print("Modulus: Cannot use zero as the divisor")
