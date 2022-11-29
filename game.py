import random

topic_list = ['animals', 'fruit', 'sports', 'random']
animals = ['Alpaca', 'Buffalo', 'Bull', 'Camel', 'Cat', 'Chicken', 'Cow', 'Deer', 'Dog', 'Donkey', 'Dove', 'Duck',
           'Emu', 'Fish', 'Goat', 'Goose', 'Hamster', 'Hen', 'Horse', 'Llama', 'Mule', 'Ostrich', 'Ox', 'Parrot',
           'Partridge', 'Pig', 'Quail', 'Rabbit', 'Reindeer', 'Rooster', 'Sheep', 'Squirrel', 'Turkey', 'Yak']
fruit = ['Orange', 'Apple', 'Avocado', 'Mango', 'Peach', 'Banana', 'Watermelon', 'Guava', 'Kiwi', 'Apricot', 'Pear',
         'Fig', 'Lemon', 'Papaya', 'Plum', 'Coconut']
sports = ['Swimming', 'Cycling', 'Tennis', 'Boxing', 'Shooting', 'Judo', 'Golf', 'Snooker', 'Basketball', 'Football',
          'Volleyball', 'Baseball', 'Gymnastics', 'Bowling', 'Athletics', 'Weightlifting', 'Fencing', 'Archery',
          'Badminton', 'Diving', 'Cricket']
topics = [animals, fruit, sports]


def hello():
    l1 = ['Hello!', 'Hi!', 'Good morning!', 'Hey, friend!']
    print(random.choice(l1))


def start_quest():
    print("Do you want to play a game?")
    ans = input('Enter yes or no: ')
    if ans == 'yes':
        print("Okay! Let's play a guessing game!")
        return(ans)
    else:
        print("Okay then. Bye.")
        return(ans)


def choose_topic():
    if ans == 'yes':
        print("Choose a topic:")
        print(', '.join(topic_list))
        topic_choice = input('Enter the topic: ')
    if topic_choice == 'animals':
        words = animals
    elif topic_choice == 'fruit':
        words = fruit
    elif topic_choice == 'sports':
        words = sports
    else:
        words = random.choice(topics)
    print("Okay! That's your word: ")
    return(words)


def rand_word():
    r_word = random.choice(words)
    sha_word = list(r_word)
    random.shuffle(sha_word)
    sha_word_low = (' '.join(sha_word))
    print(sha_word_low.lower())
    return(r_word)


def guess():
    user_word = input('Enter a word: ')
    count = 0
    while user_word != (r_word.lower()) and count != 2:
        print("No, that's not it.")
        count += 1
        if count == 1:
            print(f"HINT: First letter is '{r_word[0]}'.")
        if count == 2:
            print(f"HINT 2: First 2 letters are '{r_word[0:2]}'.")
        user_word = input('Enter a word: ')
        if count == 3:
            print("Sorry, you lost...")
    if user_word == (r_word.lower()) and count < 3:
        print('Success!')



hello()
ans = start_quest()
words = choose_topic()
r_word = rand_word()
guess()













