# Python Program to illustrate
# Hangman Game
import random
from collections import Counter

someWords = ''' delhi himachalPradesh jammu&Kashmir uttarakhand goa rajasthan maharashtra
sikkim kolkata darjeeling digha gangtok chennai karnataka hyderabad manali andaman varanasi 
kedarnath '''

someWords = someWords.split(' ')
# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a Travelling')

    for i in word:
        if i == word[0]:
           print(word[0], end=' ')
        else:
         print('_',end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word)+2
    correct = 0
    flag = 0
    try:
        while(chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            if guess in word:

                k=word.count(guess)
                for _ in range(k):
                    letterGuessed += guess



            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char , end=' ')
                    correct += 1


                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is : ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break
                    # break
                else:
                    print('_',end=' ')



        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('you lost! Try again..')
            print('The word was {}'.format(word))

    except  KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
