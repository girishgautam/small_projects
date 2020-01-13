word = 'hangman'

word_list = list(word)

empty_list = ['-'] * len(word)
display_string = str(empty_list)

print(display_string)


attempts = 6
while attempts > 0:
    if word_list == empty_list:
        break
    user_word = input('Guess an alphabet: ')

    if user_word in word:
        i = 0
        while i < len(word_list):
            if word_list[i] == user_word:
                empty_list[i] = user_word
            i+=1
        print(empty_list)

    else:
        attempts -= 1
        print('Alphabet not in the word, please try another, remaining attempts :', attempts)

print(empty_list)

# while attempts > 0:
#
#     user_word = input('Guess an alphabet: ')
#     if user_word in word:
#             # empty_list[word.index(user_word)] = user_word
#             empty_list.replace('-', user_word, len(word))
#             print(empty_list)
#     else:
#         attempts -= 1
#         print('Alphabet not in the word, please try another, remaining attempts :', attempts)
