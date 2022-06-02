import random

# setting variables

player = input('Who would you like to play the WORDLE game? Enter you if you want to play, enter AI Search if you want'
               'an AI to play ')
wordlist = []
correctlengthlist = []
user_input = input('Guess the wordle! ')
symbol_list = "`~!@#$%^&*()_+{}|[]\\=-:;'"'<,>.?"/1234567890'
# reading the file for all of the words
with open("usa.txt", "r") as all_words_file:
    for line in all_words_file.readlines():
        wordlist.append(line)



# for loop to put only words 5 letters long into the correctlengthlist
for word in wordlist:
    if len(word) == 6:
        correctlengthlist.append(word)

with open("results.txt", "w") as results_file:
    for word in correctlengthlist:
        results_file.write(f'{word}')

# line to get a randomly picked index to be the wordle word
random_index_number = random.randint(0, ((len(correctlengthlist)) - 1))
wordle_word = correctlengthlist[random_index_number]
print(wordle_word)


if player == 'you' or 'You' or 'Me':
# while statement to play the actual game
    while user_input != 'quit':
        try:
            if f'{user_input}\n' not in correctlengthlist:
                raise NameError

            #for loop to make sure only letters are entered

            for symbol in symbol_list:
                if symbol in user_input:
                    raise ValueError


            # if statement to make sure the inputted word is only 6 letters long
            if len(user_input) != 5:
                raise IndexError
                break
    # for loop to determine if the input is the correct word, or has letters in the correct spot,
    # or has any of the guessed letters in the wordle word at all
            for i in range(0, ((len(user_input)))):
                if user_input == wordle_word:
                    print(f'\nYou guessed it, the word is {wordle_word}')
                    break
                elif user_input[i] == wordle_word[i]:
                    print(f'{user_input[i]} is in the word and in the correct spot')
                elif user_input[i] in wordle_word:
                    print(f'{user_input[i]} is in the word, but not in the correct spot')
                else:
                    print(f'{user_input[i]} is not in the word')

            user_input = input('Enter another guess for the next word or enter quit to stop playing. \n')



        #except handler to deal with there being too many or too few letters in the guessed word
        except IndexError:
            print('\nMake sure your word is 5 letter long')
            user_input = input()

        except ValueError:
            print('\nMake sure your words only contain letters')
            user_input = input()

        except NameError:
            print("\nMake sure you enter a real word")
            user_input = input()



print("\nThanks for playing!")
