import random

'''make another dictionary for the future gueses to get the max score of those guessesor delete the guesses with the
 wrong letters from the word_score_dictionary'''

'''Word = timed'''
'''For the genetic algorithm, it's running correctly, the problem is how long it takes to form a word. Since there's 
five letters in the word and if each letter in the genetic algorithm guess didn't match at all in the word, which 
 isn't likely, there's still 21 letters in the alphabet and in 36 minutes and 50,213 guesses only the word "Eases" was 
 created, however the problem is that eases was the first word that was guessed, so this word was already deemed as a 
 word that isn't the solution. Additionally, eases was created about five times out of the 50,213 guesses. I wasn't sure
 if I should maybe'''

'''How do I make the wordle recognize if there's more than one letter in the wordle_word or if there's more than one of 
same letter in the user_guess or gen_alg_guess but not more than one word in the wordle_word'''

'''list for in if statement, '''
# class word_maker:
#     def __init__(self, word):
#         self.word = word
#
#     def word_maker(self):
#         self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
#         # chunk of code to find the word to guess as the wordle word
#         letter_match = 0
#         string1 = ''
#         string2 = ''
#         final_string = ''
#         while final_string not in words_only_list:
#             for letter in range(len(gen_alg_guess)):
#                 if gen_alg_guess[i] == wordle_word[i]:
#                     string1 += gen_alg_guess[i]
#                     letter_match += 1
#                 elif letter_match == 0:
#                     final_string = max(word_score_dict, key=word_score_dict.get)
#                     word_score_dict.update({gen_alg_guess: -1})
#                 elif gen_alg_guess != wordle_word[i]:
#                     string2 += random.choice(alphabet)
#             final_string = string1 + string2
#             if len(final_string) == 5:
#
#             print(final_string)
#         print(final_string)
#


# function to determine if the guessed word is correct

# determining who the user wants to play the game
player = input('Who would you like to play the WORDLE game? Enter "you" if you want to play, enter "gen" if you want'
               'a genetic algorithm AI to play ')
# initializing variables
genetic_alg_list = ['gen', 'genetic', 'genetic algorithms', 'genetic algorithm ai', 'genetic algorithm',
                    'genetic algorithm AI', 'Gen', 'Genetic', 'Genetic Algorithms', 'Genetic Algorithm']

user_list = ['me', 'ME', 'you', 'YOU', 'Me', "You"]
search_alg_list = ['Search', 'SEARCH', 'search', 'search algorithm ai', 'Search Algorithm AI', 'Search AI',
                   'search ai']
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
random_index_number = random.randint(0, ((len(correctlengthlist)) - 1))
wordle_word = words_only_list[random_index_number]
print(wordle_word)
# if satement that will run if the user wants a genetic algorithm so solve the wordle game

if player in genetic_alg_list:
    gen_alg_guess = ''
    # initializing AI variables
    letter_count_dict = {}
    count = 0
    gen_alg_list = []
    letter_count_dict = {}
    word_score_dict = {}
    # triple for loop to get the number of times each letter is used in the file for every word to create a dictionary
    # with the letter being the key and the number of times that letter was used being the value for that letter key
    for alphabet_letter in alphabet:
        count = 0
        for word in correctlengthlist:
            for letter in word:
                if letter == alphabet_letter:
                    count += 1
                letter_count_dict[alphabet_letter] = count


    # for loop to get the score of each word which is the sum of all of the letters count and make a dictionary
    # with each word as key and the corresponding score for the word as the value
    for word in words_only_list:
        word_score = 0
        for letter in word:
            word_score += letter_count_dict[letter]
        word_score_dict[word] = word_score

    # initailize variables
    gen_alg_guess = max(word_score_dict, key=word_score_dict.get)
    word_score_dict.update({gen_alg_guess: -1})
    print(gen_alg_guess, word_score_dict[gen_alg_guess])
    gen_alg_guess = 'arose'


    alphabet0 = alphabet_list.copy()
    alphabet1 = alphabet_list.copy()
    alphabet2 = alphabet_list.copy()
    alphabet3 = alphabet_list.copy()
    alphabet4 = alphabet_list.copy()
    alphabet_number_list = [alphabet0, alphabet1, alphabet2, alphabet3, alphabet4]

    # While statement to keep playing the game until the AI guesses the word
    while gen_alg_guess != wordle_word:
        # initialize some variables
        final_string = ''
        output_string = ''
        letter_match_score = 0

        # for loop to print the information on the words
        for i in range(0, (len(gen_alg_guess))):
            if gen_alg_guess == wordle_word:
                print(f'\nYou guessed it, the word is {wordle_word}')
                final_string = gen_alg_guess
                letter_match_score = 2
                break
            elif gen_alg_guess[i] == wordle_word[i]:
                print(f'{gen_alg_guess[i]} is in the word and in the correct spot')
                output_string += 'g'
                letter_match_score = 1
            elif gen_alg_guess[i] in wordle_word:
                print(f'{gen_alg_guess[i]} is in the word, but not in the correct spot')
                output_string += 'y'
                letter_match_score = 1
            else:
                print(f'{gen_alg_guess[i]} is not in the word')
                output_string += 'w'

        # chunk of code to find the word to guess as the wordle word
        # initializing variables
        string1 = ''
        string2 = ''
        word_count = 0

        # while loop to randomly guess letters until it makes a word
        while final_string not in words_only_list:

            final_string = ''
            for i in range(len(output_string)):
                if letter_match_score == 0:
                    final_string = max(word_score_dict, key=word_score_dict.get)
                    word_score_dict.update({string1: -1})

                elif output_string[i] == 'g':
                    # add the letter since it's in the correct spot to the final string
                    final_string += gen_alg_guess[i]
                    # change the score of the letter since it's in the correct spot by a multiple of 10
                    letter_count_dict[gen_alg_guess[i]] *= 10
                    # for loop to recalculate the score of the words
                    for word in words_only_list:
                        word_score = 0
                        for letter in word:
                            word_score += letter_count_dict[letter]
                        word_score_dict[word] = word_score

                elif output_string[i] == 'y':
                    # remove the letter from the same indexed list that contains all of the  possible
                    # letters to be chosen from
                    if gen_alg_guess[i] in alphabet_number_list[i]:
                        alphabet_number_list[i].remove(gen_alg_guess[i])
                    final_string += random.choice(alphabet_number_list[i])
                    # multiply the score of the individual letter by 5
                    letter_count_dict[gen_alg_guess[i]] *= 5
                    # recalculate the score of words
                    for word in words_only_list:
                        word_score = 0
                        for letter in word:
                            word_score += letter_count_dict[letter]
                        word_score_dict[word] = word_score

                elif output_string[i] == 'w':
                    for index in range(len(alphabet_number_list)):
                        if gen_alg_guess[i] in alphabet_number_list[index]:
                            alphabet_number_list[index].remove(gen_alg_guess[i])
                    final_string += random.choice(alphabet_number_list[i])


            if final_string in words_only_list:
                if word_score_dict[final_string] < word_score_dict[gen_alg_guess]:
                    words_only_list.remove(final_string)
                    final_string = ''
            word_count += 1
            print(final_string, gen_alg_guess, word_count)
        gen_alg_guess = final_string
        print(gen_alg_guess)

        # while loop to change the non-matching letters into _

        # while final_string not in words_only_list:
        #     string1 = gen_alg_guess
        #     for letter in range(len(gen_alg_guess)):
        #         if gen_alg_guess[i] == wordle_word[i]:
        #             string1 += gen_alg_guess[i]
        #             letter_match += 1
        #         elif letter_match == 0:
        #             string1 = max(word_score_dict, key=word_score_dict.get)
        #             word_score_dict.update({string1: -1})
        #         elif gen_alg_guess[i] != wordle_word[i]:
        #             string1 += '_'
        #     final_string = string1
        #     print(final_string)
        #
        #     # for loop to randomly guess letters until it creates a word
        #     for character in final_string:
        #         if character != '_':
        #             string2 += character
        #         elif character == '_':
        #             string2 += random.choice(alphabet)
        #     final_string = string2
        #
        #     gen_alg_guess = final_string

        print(gen_alg_guess)


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




# if statement so that a search algorithm can run
elif player in search_alg_list:

    search_alg_guess = ''
    # initializing AI variables
    letter_count_dict = {}
    count = 0
    letter_count_dict = {}
    word_score_dict = {}
    future_guesses_dict = {}
    # triple for loop to get the number of times each letter is used in the file for every word to create a dictionary
    # with the letter being the key and the number of times that letter was used being the value for that letter key
    for alphabet_letter in alphabet:
        count = 0
        for word in correctlengthlist:
            for letter in word:
                if letter == alphabet_letter:
                    count += 1
                letter_count_dict[alphabet_letter] = count


    # for loop to get the score of each word which is the sum of all of the letters count and make a dictionary
    # with each word as key and the corresponding score for the word as the value
    for word in words_only_list:
        word_score = 0
        for letter in word:
            word_score += letter_count_dict[letter]
        word_score_dict[word] = word_score

    # initailize variables
    search_alg_guess = 'arose'
    word_score_dict.update({search_alg_guess: -1})
    print(search_alg_guess, word_score_dict[search_alg_guess])
    guess_count = 0
    future_guesses_list = []
    wrong_letters_list = []

    # While statement to keep playing the game until the AI guesses the word
    while search_alg_guess != wordle_word:
        guess_count += 1
        # initialize some variables
        output_string = ''
        letter_match_score = 0

        # for loop to print the information on the words
        for i in range(0, (len(search_alg_guess))):
            if search_alg_guess == wordle_word:
                print(f'\nYou guessed it, the word is {wordle_word}')
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

            # for loop to go through indexes and add the words that have corresponding letters at the index to the
            # corresponding words list, maybe add words with the letters that are in the word but not correct spot to
            # this list as well or to another list. Try to pick word with the highest score
        for index in range(len(output_string)):
            if search_alg_guess == wordle_word:
                break
            elif letter_match_score < 1:
                if guess_count <= 1:
                    search_alg_guess = max(word_score_dict, key=word_score_dict.get)
                else:
                    search_alg_guess = max(future_guesses_dict, key=future_guesses_dict.get)
                word_score_dict.update({search_alg_guess: -1})
                future_guesses_dict.update({search_alg_guess: -1})
                break
            elif output_string[index] == 'g':
                letter_count_dict[search_alg_guess[index]] *= 10
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
                letter_count_dict[search_alg_guess[index]] *= 5
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


            elif output_string[index] == 'w':
                # for loop to remove words with wrong letters in them
                for word in future_guesses_list:
                    if search_alg_guess[index] in word:
                        future_guesses_list.remove(word)
                        words_only_list.remove(word)
                        del future_guesses_dict[word]
                wrong_letters_list.append(search_alg_guess[index])
        print('\n', guess_count)

        # for loop to get words that match the index of the green letters and have the yellow letters in them
        for ind in range(len(output_string)):
            if search_alg_guess == wordle_word:
                break
            elif 'g' in output_string and 'y' in output_string:
                green_index = output_string.index('g')
                yellow_index = output_string.index('y')
                for word in future_guesses_list:
                    if word[green_index] != search_alg_guess[green_index] and search_alg_guess[yellow_index] not in word:
                        future_guesses_list.remove(word)

            elif 'g' in output_string:
                green_index = output_string.index('g')
                for word in future_guesses_list:
                    if word[green_index] != search_alg_guess[green_index]:
                        future_guesses_list.remove(word)

        if search_alg_guess != wordle_word:
            if search_alg_guess in word_score_dict:
                del word_score_dict[search_alg_guess]
            if search_alg_guess in future_guesses_list:
                future_guesses_list.remove(search_alg_guess)
            if search_alg_guess in words_only_list:
                words_only_list.remove(search_alg_guess)
            search_alg_guess = max(future_guesses_dict, key=future_guesses_dict.get)
            future_guesses_dict[search_alg_guess] = -1




    for i in range(0, (len(search_alg_guess))):
        if search_alg_guess == wordle_word:
            print(f'\nYou guessed it, the word is {wordle_word}')
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



# if statement so that if the user wants to play the wordle game they can
elif player in user_list:
    count = 0
    user_input = input('Guess the wordle! ')
# while statement to play the actual game
    while user_input != 'quit' or count <= 6:
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

            count += 1
            if count == 6:
                print(f'You have no more guesses, the word was {wordle_word}')
                break

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