s = "hello world"
to_be_found = "h"
# for i in range(len(s)):
#
    # if s[i] == to_be_found:
#         print(f"{s[i]} was found at index {i}")
#         break
# else:
#     print(f"sorry i could not find you {to_be_found}")
#
for index, char in enumerate(s):
    if char == to_be_found:
        print(f"{char} was found at {index} ")
