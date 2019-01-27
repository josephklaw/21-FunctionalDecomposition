"""
Hangman.

Authors: Joseph Law and Daniel Su.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
import random
def dictionary():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    r = random.randrange(0, len(words))
    word_to_guess = words[r]
    return word_to_guess

def randomword():
    word_to_guess = dictionary()
    x = input("Please enter the minimum length of the word you would like to guess:")
    while len(word_to_guess) < int(x):
        word_to_guess = dictionary()
    else:
        return word_to_guess
def guess():
    g = input("Enter your guess:")
    guess1 = str(g)
    return guess1

def check(guess,answer, output,life):
    correct = False
    for k in range(len(answer)):
        if answer[k] == guess:
            index = k
            output[index] = answer[index]
            correct = True
            print('Your guess ' + str(guess) + ' is in the word!')
    if correct is False:
        life = int(life) - 1
    return life


def won(answer,dash,life):
    if int(life) > 0:
        if answer == dash:
            return True
        else:
            return False
def lost(life):
    if int(life) <= 0:
        return True
    else:
        return False

def playagain():
    play = input("Type YES if you would like to play again.  Type anything else if you would like to stop playing.")
    print("")
    if play == "YES":
        main()
    else:
        print("Goodbye!")


def main():
    answer = randomword()
    life = int(input("Enter the number of wrong guesses you would like to allow yourself: "))
    output = ['-']*(len(answer))
    while True:
        guess1 = guess()
        life = check(guess1,answer, output,life)
        dash =''
        for k in range(len(output)):
            dash = dash + output[k]
        print(dash)
        win_result = won(answer,dash,life)
        lost_result = lost(life)
        if win_result == True:
            print("Congratulations, you won!")
            break
        if lost_result == True:
            print("I'm sorry, you lost.")
            break
        print("You have " + str(life) + " lives remaining.")
        print("")
    playagain()
main()









####### Do NOT attempt this assignment before class! #######

