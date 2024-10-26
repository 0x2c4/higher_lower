import os
import random
from os import name, system

import art
import game_data

# global variables:
dictionary_len = len(game_data.data)
name_ = ""
follower_count_ = 0
description_ = ""
country_ = ""
question_list_01 = []
question_list_02 = []
score = 0
compare_a = 0
compare_b = 0
user_input = ""
answer = 0
correct_comparison = True

# functions:
def dictionary_selector(dictionary_len_pass):
    """This function will generate a random int, and use it select a random dictionary from game_data.data, then it will return the values of each key as variables named as the keys"""
    data_values = []
    random_int = random.randint(0, dictionary_len_pass)
    selected_values = game_data.data[random_int]
    name__ = selected_values["name"]
    follower_count__ = int(selected_values["follower_count"])
    description__ = selected_values["description"]
    country__ = selected_values["country"]
    data_values.append(name__)
    data_values.append(description__)
    data_values.append(country__)
    data_values.append(follower_count__)

    return data_values

def check_answer(value_a, value_b):
    """This function will compare two numeric values, and return the one which is higher"""
    correct_answer = max(value_a, value_b)

    return correct_answer

def clear():
    """This function will clear the screen"""
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


# body:
print(art.logo)
question_list_01 = dictionary_selector(dictionary_len)
compare_a = question_list_01[-1]

while correct_comparison:
    print(f"Compare A: {question_list_01[0]}, a {question_list_01[1]}, from {question_list_01[2]}")
    print(art.vs)

    question_list_02 = dictionary_selector(dictionary_len)
    compare_b = question_list_02[-1]
    print(f"Compare B: {question_list_02[0]}, a {question_list_02[1]}, from {question_list_02[2]}")

    answer = check_answer(compare_a, compare_b)
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == "a":
        if compare_a == answer:
            score += 1
            clear()
            print(art.logo)
            print(f"You're right! Current score: {score}.")
        else:
            correct_comparison = False
    elif user_input == "b":
        if compare_b == answer:
            compare_a = compare_b
            question_list_01 = question_list_02
            score += 1
            clear()
            print(art.logo)
            print(f"You're right! Current score: {score}.")
        else:
            correct_comparison = False
    else:
        print("Sorry, that's not a valid input, this program will now terminate")
        quit()

clear()
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")
