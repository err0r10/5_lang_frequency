import sys
from collections import Counter
from os.path import exists, isfile
from re import findall


def load_data(filepath):
    with open(filepath, "r") as opened_file:
        return opened_file.read()


def get_most_frequent_words(text):
    count_words = 10
    list_words = findall("\w+", text)
    words = Counter(list_words)
    return words.most_common(count_words)


def print_top_words(words):
    for word in words:
        print("{0:20} : {1}".format(*word))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not exists(sys.argv[1]):
        sys.exit("The file doesn't exist!")
    file_path = sys.argv[1]
    if isfile(file_path):
        file_data = load_data(file_path).lower()
        top_frequency_words = get_most_frequent_words(file_data)
        print_top_words(top_frequency_words)
    else:
        print("The file doesn't exist!")
