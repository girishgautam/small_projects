import random

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret ' \
        'fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python' \
        ' rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle' \
        ' weasel whale wolf wombat zebra'.split()

word = random.choice(words)

word_list = list(word)
# print(word_list)

empty_list = ['-'] * len(word_list)
# display_string = str(empty_list)

print(word)


attempts = 2
while attempts > 0:
    if word_list == empty_list:
        break
    user_word = input('Guess an alphabet: \n')

    if user_word in word_list:
        i = 0
        while i < len(word_list):
            if word_list[i] == user_word:
                empty_list[i] = user_word
            i+=1
        print(empty_list,'\n')



    else:
        attempts -= 1
        if attempts == 0:
            print('Sorry, no more attempts left. The word was', word.upper())
        else:
            print('Alphabet not in the word, please try another, remaining attempts :', attempts)




# print(empty_list)

