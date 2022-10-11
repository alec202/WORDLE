import random


# determining who the user wants to play the game
player = input('Who would you like to play the WORDLE game? Enter "you" if you want to play, enter "search" if you want'
               'a search algorithm AI to play ').upper()
# initializing variables
user_list = ['me', 'ME', 'you', 'YOU', 'Me', "You"]
search_alg_list = ['Search', 'SEARCH', 'search', 'search algorithm ai', 'Search Algorithm AI', 'Search AI',
                   'search ai', "SEARCH ALGORITHM AI", "SEARCH ALGORITHM", "SEARCH AI", "AI", ]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']
wordlist = []
correctlengthlist = []
symbol_list = "`~!@#$%^&*()_+{}|[]\\=-:;'"'<,>.?"/1234567890'
words_only_list = []

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

    # for loop to make a words list that only has the words and not the \n key so that way a dictionary with the words
    # and their corresponding scores can be made

for word in correctlengthlist:
    if "'" not in word:
        split_word = word.split('\n')
        words_only_list.append(split_word[0])

# line to get a randomly picked index to be the wordle word
random_index_number = random.randint(0, len(correctlengthlist))
wordle_word = words_only_list[random_index_number]

# wordle_word = 'wafts'
# initialize some variables for the multiple letter check
letter_appearance_dict = {}
wordle_letter_one_list = []
dict_number_value = 0
duplicate_letter_appearance = 0
dup_letter_dict = {}
# wordle_word = "cough"
# for loop to check if there are duplicate letters in the wordle_word
for letter in wordle_word:
    dict_number_value = 0
    if letter in letter_appearance_dict:
        letter_appearance_score = letter_appearance_dict[letter]
        letter_appearance_score += 1
        letter_appearance_dict[letter] = letter_appearance_score
    else:
        letter_appearance_dict[letter] = 1

# variables for the multiple letters check
multiple_appearance_dict = {}
multiple_score = 0
double_letters_dict = {}


# if statement so that a search algorithm can run
if player in search_alg_list:
    try:

        search_alg_guess = 'arose'
        # initializing AI variables
        letter_count_dict = {}
        count = 0
        letter_count_dict = {}
        word_score_dict = {}
        future_guesses_dict = {}
        search_alg_letters_dict = {}
        # dictionary with each of the letters scores
        letter_count_dict = {'q': 1, 'j': 2, 'z': 3, 'x': 4, 'v': 5, 'w': 6, 'f': 7, 'k': 8, 'g': 9, 'b': 10, 'h': 11,
                             'm': 12, 'y': 13, 'p': 14, 'c': 15, 'u': 16, 'd': 17, 'n': 18, 't': 19, 'i': 20, 'l': 21,
                             'o': 22, 'r': 23, 'a': 24, 's': 25, 'e': 26}



        # for loop to get the score of each word which is the sum of all of the letters count and make a dictionary
        # with each word as key and the corresponding score for the word as the value
        for word in words_only_list:
            word_score = 0
            for letter in word:
                word_score += letter_count_dict[letter]
            word_score_dict[word] = word_score

        # initailize variables
        word_score_dict.update({search_alg_guess: -1})
        guess_count = 0
        future_guesses_list = []
        wrong_letters_list = []
        search_alg_letters_dict_orig = {}

        # While statement to keep playing the game until the AI guesses the word
        while search_alg_guess != wordle_word:

            search_alg_letters_dict = search_alg_letters_dict_orig.copy()
            letter_appearance_dict_copy = letter_appearance_dict.copy()

            for letter in search_alg_guess:
                dict_number_value = 0
                if letter in search_alg_letters_dict:
                    letter_appearance_score = search_alg_letters_dict[letter]
                    letter_appearance_score += 1
                    search_alg_letters_dict[letter] = letter_appearance_score
                else:
                    search_alg_letters_dict[letter] = 1

            guess_count += 1
            # initialize some variables
            output_string = ''
            letter_match_score = 0

            # for loop to print the information on the words
            for i in range(0, (len(search_alg_guess))):
                if search_alg_guess == wordle_word:
                    print(f'{search_alg_guess[0]} is in the word and in the correct spot')
                    print(f'{search_alg_guess[1]} is in the word and in the correct spot')
                    print(f'{search_alg_guess[2]} is in the word and in the correct spot')
                    print(f'{search_alg_guess[3]} is in the word and in the correct spot')
                    print(f'{search_alg_guess[4]} is in the word and in the correct spot')
                    print(f'\nYou guessed it, the word is {wordle_word}')
                    letter_match_score = 2
                    break
                elif search_alg_guess[i] == wordle_word[i] and letter_appearance_dict_copy[search_alg_guess[i]] > 0:
                    print(f'{search_alg_guess[i]} is in the word and in the correct spot')
                    output_string += 'g'
                    letter_match_score = 1
                    letter_appearance_dict_copy[search_alg_guess[i]] -= 1
                elif search_alg_guess[i] in wordle_word and letter_appearance_dict_copy[search_alg_guess[i]] > 0:
                    print(f'{search_alg_guess[i]} is in the word, but not in the correct spot')
                    output_string += 'y'
                    letter_match_score = 1
                    letter_appearance_dict_copy[search_alg_guess[i]] -= 1
                else:
                    print(f'{search_alg_guess[i]} is not in the word')
                    output_string += 'w'

                # for loop to go through indexes and add the words that have corresponding letters at the index to the
                # corresponding words list, maybe add words with the letters that are in the word but not correct spot to
                # this list as well or to another list. Try to pick word with the highest score
            for index in range(len(output_string)):
                # if 'g' in output_string and 'y' in output_string:
                #     g_letter_index = output_string.index('g')
                #     y_letter_index = output_string.index('y')
                #     for inde in range(len(output_string)):

                if search_alg_guess == wordle_word:
                    break
                elif output_string[index] == 'g':
                    letter_count_dict[search_alg_guess[index]] *= 2000
                    # recalculate the score of words
                    for word in words_only_list:
                        word_score = 0
                        for letter in word:
                            word_score += letter_count_dict[letter]
                        word_score_dict[word] = word_score
                    # append words that have the green letter in the correct spots to the future guesses list
                    for word in words_only_list:
                        if word[index] == search_alg_guess[index] and word not in future_guesses_list:
                            future_guesses_list.append(word)
                            future_guesses_dict[word] = word_score_dict[word]
                elif output_string[index] == 'y':
                    letter_count_dict[search_alg_guess[index]] *= 35
                    # recalculate the score of words
                    for word in words_only_list:
                        word_score = 0
                        for letter in word:
                            word_score += letter_count_dict[letter]
                        word_score_dict[word] = word_score
                        # append words that have the yellow letter in them to the future guesses list
                    for word in words_only_list:
                        if search_alg_guess[index] in word and word not in future_guesses_list:
                            future_guesses_list.append(word)
                            future_guesses_dict[word] = word_score_dict[word]
                    if 'g' in output_string:
                        g_letter_index = output_string.index('g')
                        for key in future_guesses_dict:
                            if key[g_letter_index] != search_alg_guess[g_letter_index]:
                                future_guesses_dict[key] = -1
                    for key in future_guesses_dict:
                        for letter in wrong_letters_list:
                            if letter in key:
                                future_guesses_dict[key] = -1

                elif output_string[index] == 'w':
                    if search_alg_guess[index] not in wordle_word:
                        # for loop to remove words with wrong letters in them
                        for word in word_score_dict:
                            if search_alg_guess[index] in word:
                                word_score_dict[word] = -1

                        for key in future_guesses_dict:
                            if search_alg_guess[index] in key:
                                future_guesses_dict[key] = -1

                        wrong_letters_list.append(search_alg_guess[index])

            print(f'Guess: {guess_count} \n')

            # for loop to get words that match the index of the green letters and have the yellow letters in them
            for ind in range(len(output_string)):
                if search_alg_guess == wordle_word:
                    break
                elif letter_match_score < 1:
                    break
                elif 'g' in output_string and 'y' in output_string:
                    green_index = output_string.index('g')
                    yellow_index = output_string.index('y')
                    for key in future_guesses_dict:
                        if key[green_index] != search_alg_guess[green_index] or search_alg_guess[yellow_index] not in key:
                            future_guesses_dict[key] = -1
                # if statements to give words with letters in the wrong spot or words with none of the yellow/green
                # letters in them a score of -1
                if output_string[ind] == 'g':
                    green_index = ind
                    for key in future_guesses_dict:
                        if key[green_index] != search_alg_guess[green_index]:
                            future_guesses_dict[key] = -1
                        if search_alg_guess[green_index] not in key:
                            future_guesses_dict[key] = -1
                        if key[green_index] == search_alg_guess[green_index]:
                            future_guesses_dict[key] *= 500
                if output_string[ind] == 'y':
                    yel_letter_index = ind
                    for key in future_guesses_dict:
                        if key[yel_letter_index] == search_alg_guess[yel_letter_index]:
                            future_guesses_dict[key] = -1
                        if search_alg_guess[yel_letter_index] not in key:
                            future_guesses_dict[key] = -1


            for key in future_guesses_dict:
                for letter in wrong_letters_list:
                    if letter in key:
                        future_guesses_dict[key] = -1


            if search_alg_guess != wordle_word:
                if search_alg_guess in word_score_dict:
                    del word_score_dict[search_alg_guess]
                if search_alg_guess in future_guesses_dict:
                    future_guesses_dict[search_alg_guess] = -1
                if search_alg_guess in future_guesses_list:
                    future_guesses_list.remove(search_alg_guess)
                if search_alg_guess in words_only_list:
                    words_only_list.remove(search_alg_guess)



            if letter_match_score < 1 or output_string == 'wwwww':
                word_score_dict.update({search_alg_guess: -1})
                future_guesses_dict.update({search_alg_guess: -1})
                search_alg_guess = max(word_score_dict, key=word_score_dict.get)
            else:
                search_alg_guess = max(future_guesses_dict, key=future_guesses_dict.get)

            if guess_count > 50:
                raise ValueError




        guess_count += 1
        for i in range(0, (len(search_alg_guess))):
            if search_alg_guess == wordle_word:
                print(f'{search_alg_guess[0]} is in the word and in the correct spot')
                print(f'{search_alg_guess[1]} is in the word and in the correct spot')
                print(f'{search_alg_guess[2]} is in the word and in the correct spot')
                print(f'{search_alg_guess[3]} is in the word and in the correct spot')
                print(f'{search_alg_guess[4]} is in the word and in the correct spot')
                if guess_count == 1:
                    print(f'\nYou guessed it in {guess_count} guess, the word is {wordle_word}')
                else:
                    print(f'\nYou guessed it in {guess_count} guesses, the word is {wordle_word}')

                final_string = search_alg_guess
                letter_match_score = 2
                break
            elif search_alg_guess[i] == wordle_word[i]:
                print(f'{search_alg_guess[i]} is in the word and in the correct spot')
                output_string += 'g'
                letter_match_score = 1
            elif search_alg_guess[i] in wordle_word:
                print(f'{search_alg_guess[i]} is in the word, but not in the correct spot')
                output_string += 'y'
                letter_match_score = 1
            else:
                print(f'{search_alg_guess[i]} is not in the word')
                output_string += 'w'
    except Exception as e:
        print(e)


# if statement so that if the user wants to play the wordle game they can
elif player in user_list:
    user_input = input('Guess the wordle! ')
    count = 1
# while statement to play the actual game
    while user_input != wordle_word and count <= 6:
        letter_appearance_dict_copy = letter_appearance_dict.copy()
        try:
            #for loop to make sure only letters are entered
            for symbol in symbol_list:
                if symbol in user_input:
                    raise ValueError


            # if statement to make sure the inputted word is only 6 letters long
            if len(user_input) != 5:
                raise IndexError
                break

            # if statement to make sure that the entered letters ake an actual word
            if user_input not in words_only_list:
                raise NameError

     # for loop to determine if the input is the correct word, or has letters in the correct spot,
     # or has any of the guessed letters in the wordle word at all
            for i in range(0, ((len(user_input)))):
                if user_input == wordle_word:
                    print(f'{user_input[0]} is in the word and in the correct spot')
                    print(f'{user_input[1]} is in the word and in the correct spot')
                    print(f'{user_input[2]} is in the word and in the correct spot')
                    print(f'{user_input[3]} is in the word and in the correct spot')
                    print(f'{user_input[4]} is in the word and in the correct spot')
                    print(f'\nYou guessed it, the word is {wordle_word}')
                    break
                elif user_input[i] == wordle_word[i] and letter_appearance_dict_copy[user_input[i]] > 0:
                    print(f'{user_input[i]} is in the word and in the correct spot')
                    letter_appearance_dict_copy[user_input[i]] -= 1
                elif user_input[i] in wordle_word and letter_appearance_dict_copy[user_input[i]] > 0:
                    print(f'{user_input[i]} is in the word, but not in the correct spot')
                    letter_appearance_dict_copy[user_input[i]] -= 1
                else:
                    print(f'{user_input[i]} is not in the word')

            count += 1
            if count == 7:
                print(f'\nYou have no more guesses, the word was {wordle_word}')
                break
            user_input = input(f'Enter another guess, you have {7 - count} guesses remaining.\n')
            if user_input == wordle_word:
                print(f'{user_input[0]} is in the word and in the correct spot')
                print(f'{user_input[1]} is in the word and in the correct spot')
                print(f'{user_input[2]} is in the word and in the correct spot')
                print(f'{user_input[3]} is in the word and in the correct spot')
                print(f'{user_input[4]} is in the word and in the correct spot')
                print(f'\nYou guessed it, the word is {wordle_word}')




        # except handler to deal with there being too many or too few letters in the guessed word
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