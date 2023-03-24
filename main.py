# This function prompts the user to input six numbers and return a list of them
from random import shuffle


def get_player_numbers() -> list[int]:
    print("Provide six unique numbers in range of 1 to 49.")
    numbers = []
    while len(numbers) < 6:
        n = input("Please, provide a number: ")
        if validate_number(n, numbers):
            numbers.append(int(n))
        else:
            print("You need to provide a unique number from 1 to 49")
    return numbers


# Checks if the number provided by the user is an int in range of 1 to 49, that does not already exist in the list
def validate_number(num:str, num_list: list[int]) -> bool:
    try:
        n = int(num)
    except ValueError:
        return False
    if (not 1 <= n <= 49) or (n in num_list):
        return False
    return True


# Generates a list of six winning numbers
def get_lotto_numbers() -> list[int]:
    numbers = list(range(1, 50))
    shuffle(numbers)
    return sorted(numbers[:6])


# Compares the numbers inputted by the user with the generated ones, and returns the number of the correct guesses
def get_correct_guesses(player_nums:list[int], lotto_nums:list[int]) -> int:
    correct = 0
    for i in player_nums:
        if i in lotto_nums:
            correct += 1

    return correct


player_numbers = sorted(get_player_numbers())
lotto_numbers = get_lotto_numbers()

print(player_numbers)
print(lotto_numbers)

correct_guesses = get_correct_guesses(player_numbers, lotto_numbers)
print(f"You have managed to guess {correct_guesses} numbers correctly.")



