#counter = 0
# for counter in range(1, 101, 1):
#     if counter % 15 == 0:
#         print("FizzBuzz")
#     elif counter % 3 == 0:
#         print("Fizz")
#     elif counter % 5 == 0:
#         print("Buzz")
#     else:
#         print(counter)

# number = int(input("Enter a number: "))
# counter = 1
# sum_of_counter = 0
# while number < counter:
#     if number % counter == 0:
#         sum_of_counter += counter
#     counter += 1
#
#     if sum_of_counter < number:
#         prin t(number, "is deficient")
#     elif sum_of_counter > number:
#         print(number, "is abundant")
#     else:
#         print(number, "is a perfect number")
    #print (counter + number)

# i = "Mississippi is the longest river"
#
# print(i[:11:])
# print(i[-5:])
# print(i[15:18])
# print(i[0:20:4])
# print(i[:18:-1])
# print(i[::-1])

name = "Renike"
age = 12

s = "{} is {} years old" .format(name, age)
p = "{0} is {1} years old, and {0} loves {2}" .format(name, age, "Java")
r = "{0:^20} is {1:>10.2f} years old, and {0} loves {2}" .format(name, age, "Java")
t = f"{name:^20} is {age:>10.2f} years old, and {name} loves {'Java'}"
print(s)
print(p)
print(r)
print(t)

for i in range(1, 21, 2):
    s = "*" * i
    print(f"{s:20}{s:^20}{s:>20}")

hello = "hello world"
for i, l in enumerate(hello, start=1):
    print(f"{l}---> {i}")

for index in range(len(hello)):
    print(f"{hello[index]}---> {index}")

word = "my cohort is great"
for word in word:
    print(word[:20], end="  ")
    
    print(len(word))



