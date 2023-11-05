import random


def load_file(file_name):
    with open(file_name, "r") as file:
        words = file.readlines()
    return words


def select_random_word(words):
    word_index = random.randint(0, len(words)-1)
    random_word = words[word_index]
    return random_word


def select_random_letter(word):
    letter_index = random.randint(0, len(word) - 1)
    random_letter = word[letter_index]
    updated_word = word.replace(random_letter, "_")
    print("Guess the letter:", updated_word)
    return random_letter, letter_index


def get_user_input():
    user_input = input("Guess the missing letter:")
    return user_input


def show_correctness(answer, word, missing_letter_index):
    if answer == word[missing_letter_index]:
        message = f'The word was:{word}\nWell Done! You are awesome'
    else:
        message = f'The word was:{word}\nWrong! Do beter next time'
    print(message)


def ask_file_name():
    file_input = input("Words file? [leave empty to use short_words.txt]:")
    if file_input == "":
        return "random_words.txt"
    else:
        return file_input


def run_game(file_name):
    words = load_file(file_name)
    word = select_random_word(words)
    random_letter, letter_index = select_random_letter(word)
    answer = get_user_input()
    show_correctness(answer, word, letter_index)

    print('The word was: '+word)


if __name__ == "__main__":
    word_files = ask_file_name()
    run_game(word_files)
