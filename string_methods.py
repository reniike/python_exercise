#hello = "Hello there!!!"
#
# print(hello.find("l", 3))
# print(hello.find("e", 3, 5))
# print(hello.index("t"))

# for count in range (1, 10, 2):
#     asterisks = "*" * count
#     print(asterisks.center(9))

# print(hello.startswith("H"))
# print("-".join(["a", "b", "c"]))
#bin()

#cipher_algo
import string

user_input = input("Enter the word to decode: ")
key = int(input("What key would you like to use: "))

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

decoded_lower_letters = lower_letters[key:] + lower_letters[:key]
decoded_upper_letters = upper_letters[key:] + upper_letters[:key]

letters = lower_letters + upper_letters + string.whitespace
decoded_letters = decoded_lower_letters + decoded_upper_letters + string.whitespace

encoded = user_input.translate(str.maketrans(letters, decoded_letters))
decoded = encoded.translate(str.maketrans(decoded_letters, letters))
#print(user_input.translate(str.maketrans(lower_letters + "", decoded_letters + "")))

print(encoded)
print(decoded)


