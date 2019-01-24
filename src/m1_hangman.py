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

def check(guess,answer, output):
    for k in range(len(answer)):
        if answer[k] == guess:
            index = k
            output[index] = answer[index]











def main():
    answer = randomword()
    print(answer)
    output = ['-']*(len(answer))
    guess1 = guess()
    check(guess1,answer, output)
    dash =''
    for k in range(len(output)):
        dash = dash + output[k]
    print(dash)
main()










####### Do NOT attempt this assignment before class! #######

