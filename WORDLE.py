import random

# function to determine if the guessed word is correct

# determining who the user wants to play the game
player = input('Who would you like to play the WORDLE game? Enter "you" if you want to play, enter "AI" if you want'
               'a genetic algorithm AI to play ')
# initializing variables
alphabet = 'abcdefghijklmnopqrstuvwxyz'
wordlist = []
correctlengthlist = []
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

# if satement that will run if the user wants a genetic algorithm so solve the wordle game

if player == 'AI' or 'ai':
    gen_alg_guess = ''
    # initializing AI variables
    letter_count_dict = {}
    count = 0
    gen_alg_list = []
    letter_count_dict = {}
    word_score_dict = {}
    words_only_list = []
    # triple for loop to get the number of times each letter is used in the file for every word to create a dictionary
    # with the letter being the key and the number of times that letter was used being the value for that letter key
    for alphabet_letter in alphabet:
        count = 0
        for word in correctlengthlist:
            for letter in word:
                if letter == alphabet_letter:
                    count += 1
                letter_count_dict[alphabet_letter] = count

    # for loop to make a words list that only has the words and not the \n key so that way a dictionary with the words
    # and their corresponding scores can be made
    for word in correctlengthlist:
        if "'" not in word:
            split_word = word.split('\n')
            words_only_list.append(split_word[0])

    # for loop to get the score of each word which is the sum of all of the letters count and make a dictionary
    # with each word as key and the corresponding score for the word as the value
    for word in words_only_list:
        word_score = 0
        for letter in word:
            word_score += letter_count_dict[letter]
        word_score_dict[word] = word_score

    # While statement to keep playing the game until the user quits
    while gen_alg_guess != wordle_word:
        gen_alg_guess = max(word_score_dict, key=word_score_dict.get)
        word_score_dict.update({gen_alg_guess: -1})
        print(gen_alg_guess, word_score_dict[gen_alg_guess])

        for i in range(0, ((len(gen_alg_guess)))):
            if gen_alg_guess == wordle_word:
                print(f'\nYou guessed it, the word is {wordle_word}')
                break
            elif gen_alg_guess[i] == wordle_word[i]:
                print(f'{gen_alg_guess[i]} is in the word and in the correct spot')
            elif gen_alg_guess[i] in wordle_word:
                print(f'{gen_alg_guess[i]} is in the word, but not in the correct spot')
            else:
                print(f'{gen_alg_guess[i]} is not in the word')



        for letter in gen_alg_guess:
            if letter == "correct spot":
                gen_alg_guess


        gen_alg_guess = max(word_score_dict, key=word_score_dict.get)

        # except handler to deal with there being too many or too few letters in the guessed word
        gen_alg_guess = input()


# if statement so that if the user wants to play the wordle game they can
elif player == 'you' or 'You' or 'Me':
    user_input = input('Guess the wordle! ')
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