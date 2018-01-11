import sys
from collections import Counter
from os.path import exists, isfile
from re import compile, findall

COUNT_FREQUENCY = 10


def load_data(filepath):
    with open(filepath, 'r') as opened_file:
        return opened_file.read()


def get_most_frequent_words(text, counter):
    regular = compile("\w+")
    clean_terxt = findall(regular, text)
    word = Counter(clean_terxt)
    return word.most_common(counter)


if __name__ == '__main__':
    file_path = sys.argv[1]
    if exists(file_path) and isfile(file_path):
        text = load_data(file_path).lower()
        frequency_word_ten = get_most_frequent_words(text, COUNT_FREQUENCY)
        print(frequency_word_ten)
    else:
        print("The file doesn't exist!")
