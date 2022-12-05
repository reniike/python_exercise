number = int(input("Enter number: "))
largest_number = number
second_largest_number = number
counter = 1

while counter <= 5:
    if number > largest_number:
        large = largest_number
        largest_number = number
        second_largest_number = large
    number = int(input("Enter number: "))
    counter += 1

print("largest number is", largest_number)
print("second largest number is", second_largest_number)

