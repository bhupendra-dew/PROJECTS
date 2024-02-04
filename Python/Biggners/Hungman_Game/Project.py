import random
from collections import Counter

someWords = "apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon"

someWords = someWords.split(' ')

word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')
    for i in word:
        print('_', end = ' ')
    print()

    playing = True

    letterGuessed = ""
    chnaces = len(word) + 2
    correct = 0
    flag = 0

    try:
        while (chnaces != 0) and flag == 0:
            print()
            chnaces -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print("Enter only a letter !")
                continue

            if not guess.isalpha():
                print("Enter only a Letter")
                continue
            
            elif len(guess) & gt 1:
                print("Enter only a single letter")
                continue

    except:            