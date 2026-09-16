print("----- Numbers from 1 to 20 -----")
for number in range(1, 21):
    print(number, end=" ")

print("\n\n----- Multiplication Table -----")
table_number = int(input("Enter a number: "))
for multiplier in range(1, 11):
    print(table_number, "x", multiplier, "=", table_number * multiplier)

print("\n----- Even Numbers from 1 to 50 -----")
number = 2
while number <= 50:
    print(number, end=" ")
    number += 2
print()
