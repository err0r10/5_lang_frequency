import sys
from collections import Counter
from os.path import exists, isfile
from re import compile, findall
from config import count_out_words


def load_data(filepath):
    with open(filepath, 'r') as opened_file:
        return opened_file.read()


def get_most_frequent_words(text, count_words):
    find_words = findall("\w+", text)
    words = Counter(find_words)
    return words.most_common(count_words)


def print_top_words(words):
    for word in words:
        print(
            "Word = {0}, Count={1}".format(word[0], word[1])
        )


if __name__ == '__main__':
    file_path = sys.argv[1]
    if exists(file_path) and isfile(file_path):
        file_data = load_data(file_path).lower()
        top_frequency_words = get_most_frequent_words(
            file_data,
            count_out_words
        )
        print_top_words(top_frequency_words)
    else:
        print("The file doesn't exist!")
