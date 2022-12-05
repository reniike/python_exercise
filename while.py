#x: int = 0

#while x < 10:
    #print(x, end=" ")
    #x += 1

#print()
#print("The final value is", x)

count = 0
largest_so_far  = 0
while count < 5:
    num = int(input("Give me a number: "))
    if num > largest_so_far:
        largest_so_far = num

        count += 1

#count = 0
#3smallest_so_far