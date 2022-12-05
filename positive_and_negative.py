userinput = int(input("Enter a number, the input ends if its 0:  "))

negative_count = 0
positive_count = 0
sum_of_userinput = 0
average = 0

while userinput != 0:
    if userinput < 0:
        negative_count = negative_count + 1
    if userinput > 0:
        positive_count = positive_count + 1

    sum_of_userinput += userinput
    sum_of_numbers = negative_count + positive_count
    average = sum_of_userinput / sum_of_numbers

    userinput = int(input("Enter a number, the input ends if its 0: "))

if sum_of_userinput == 0:
    print("No numbers are entered except 0.")
else:
    print("The number of negative is: ", negative_count)
    print("The number of positive is: ", positive_count)
    print("The total is: ", float(sum_of_userinput))
    print("The average is: ", float(average))
