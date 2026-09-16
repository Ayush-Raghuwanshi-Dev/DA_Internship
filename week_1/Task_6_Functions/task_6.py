def square(number):
    return number * number


def average(first_number, second_number, third_number):
    return (first_number + second_number + third_number) / 3


number = float(input("Enter a number to find its square: "))
first_number = float(input("Enter the first number for the average: "))
second_number = float(input("Enter the second number for the average: "))
third_number = float(input("Enter the third number for the average: "))

print("\nSquare:", square(number))
print("Average:", average(first_number, second_number, third_number))
