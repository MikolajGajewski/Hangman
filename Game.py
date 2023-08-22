import sys
import random
import os

life = 10;

words_list = []
user_word = []
user_letters = []
file_path = "words.txt"

with open(file_path, "r") as file:
    for line in file:

        word = line.strip()
        words_list.append(word)

def restart():
    answer=input("Czy chcesz spróbować jeszcze raz? Y/N: ").upper()
    if answer == "Y":
        print("yes")

def find_indexes(word, letter):
    indexes= []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes;

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób: ", life)
    print("Użyte litery", user_letters)
    print() 


words = random.choice(words_list)
        

for _ in words:
    user_word.append("_")

while True:
    letter=input("Podaj literę: ")
    if len(letter)!=1:
        print("Wpisz tylko jedną literę na raz")
        continue;
    elif letter.isalpha():
        user_letters.append(letter)
    else:
        print("Słowa składają się tylko z liter. Tym razem wpisz literę z kórej może się składać hasło.")
        continue;  
    
    found_indexes = (find_indexes(words, letter))

    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        life -= 1

        if life == 0:
            print("")
            print("Game Over")
            restart()

    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == words:
            print("")
            print ("Congratulations!")
            sys.exit(0)

    show_state_of_game()