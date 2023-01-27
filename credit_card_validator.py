user_input = input("Enter Credit Card Number: ")


def card_length_validator(card_number):
    if len(card_number) <= 13 or len(card_number) > 16:
        return "Invalid length"
    else:
        return "Valid length"


def card_confirmation(card_number):
    total_of_sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for i in range(len(card_number) - 2, -1, -2):
        sum_of_even_digits = (int(card_number[i]) * 2)
        if sum_of_even_digits > 9:
            sum_sum = (sum_of_even_digits % 10) + (sum_of_even_digits // 10)
            total_of_sum_of_even_digits = total_of_sum_of_even_digits + sum_sum
        else:
            total_of_sum_of_even_digits = total_of_sum_of_even_digits + sum_of_even_digits
    for i in range(len(card_number) - 1, -1, -2):
        sum_of_odd_digits += (int(card_number[i]))
    if ((total_of_sum_of_even_digits + sum_of_odd_digits) % 10) == 0:
        return "Card is Valid"
    else:
        return "Card is Invalid"


def card_type(card_number):
    if card_number.startswith("4"):
        return "Visa Card"
    if card_number.startswith("5"):
        return "Master Card"
    if card_number.startswith("37"):
        return "American Express Card"
    if card_number.startswith("6"):
        return "Discover Card"
    else:
        return "Invalid Card Type"


print("********************")
print("** Card Length:- ", card_length_validator(user_input))
print("** Credit Card Type:- ", card_type(user_input))
print("** Credit Card Number:- ", user_input)
print("** Credit Card Validity:- ", card_confirmation(user_input))
print("********************")