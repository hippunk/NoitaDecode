from natsort import natsorted, ns
import os
from numpy import random

def load_as_array(path):
    inList = natsorted(os.listdir(path), alg=ns.PATH)
    message = {}
    for filename in inList:

        filename_without_ext = os.path.splitext(filename)[0]
        filename_tokens = filename_without_ext.split('_')
        x = int(filename_tokens[1])
        y = int(filename_tokens[0])
        orientation = filename_tokens[2]
        if y not in message:
            message[y] = {}
        message[y][x] = orientation

    return message

def transform_to_trigram(message):
    trigrams = []
    i = 0
    while i < len(message):
        trigrams_line = []
        j = 0
        while j < len(message[i]):

            trigrams_line.append([message[i][j], message[i][j + 1], [message[i + 1][j]]])
            if j + 2 < len(message[i]):
                trigrams_line.append([message[i + 1][j + 1], message[i + 1][j + 2], [message[i][j + 2]]])
            j += 3

        trigrams.append(trigrams_line)
        i += 2
    return trigrams

def parse_trigrams_to_numeric(trigrams):
    val = []
    for trigram_line in trigrams:
        line = []
        for trigram in trigram_line:
            if trigram is not "\n":
                count = 0
                for char in trigram:
                    if isinstance(char, list):
                        # Here there's an option to compute special operation through key value
                        char = char[0]
                    if char == 'N':
                        count += 1
                    if char == 'S':
                        count += 10
                    if char == 'W':
                        count += 100
                    if char == 'E':
                        count += 1000
                    if char == 'C':
                        count += 10000
                line.append(count)
        val.append(line)

    return val

def pretty_print_message(message):
    for coord_x in message:
        str = ""
        for coord_y in message[coord_x]:
            str += message[coord_x][coord_y] + " "
        print(str)
    print("") #line return


def pretty_print_trigrams(trigrams):
    text = ""
    for trigram_line in trigrams:
        for trigram in trigram_line:
            text += str(trigram) + " "
        text += '\n'
    print(text)


def pretty_print_values(values):
    text = ""
    for value_line in values:
        for value in value_line:
            text += "{0:>6}".format(value) + " "
        text += '\n'
    print(text)


def catch_unique(list_in):
    unq_list = []

    # Check for elements
    for x in list_in:
        # check if exists in unq_list
        if x not in unq_list:
            unq_list.append(x)
            # print list
    return unq_list


def sort_dict(dict):
    sorted_dict = {}
    sorted_list = []
    sorted_keys = sorted(dict, key=dict.get,reverse=True)  # [1, 3, 2]

    for w in sorted_keys:
        sorted_dict[w] = dict[w]
        sorted_list.append(w)

    return sorted_dict,sorted_list


def compute_list_frequency(list):
    frequency = {}
    for item in list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

def get_finish_dict():
    words = []
    with open('finnish_dictionary.txt', encoding='utf8') as f:
        for word in f.readlines():
            words.append(word.replace('\n', ''))
    return words

#https://www.sttmedia.com/characterfrequency-finnish
most_frequent_finnish_letters = ['A', 'I', 'T', 'N', 'E', 'S', 'O', 'L', 'Ä', 'K', 'U', 'M', 'H', 'V', 'R', 'J', 'P', 'Y', 'D', 'Ö', 'G', 'C', 'B', 'F', 'W', 'Z', 'X', 'Å', 'Q', 'Š', 'Ž']

def test_permutation(values,frequency_list,permutation,word_dic,show_text):
    raw_text = " "
    cpt_match = 0
    for val in values:
        if val in frequency_list:
            indexFreq = frequency_list.index(val)
            raw_text += permutation[indexFreq]
        else:
            raw_text += "\n"

    for word in word_dic:
        if word in raw_text:
            cpt_match += 1
    if show_text == True:
        print(raw_text)
    print("Word match number : " + str(cpt_match))

def do_random_permutations(values,frequency_list,permutation,word_dic,n = 10000):
    best = 0
    for i in range(n):
        random.shuffle(permutation)
        raw_text = ""
        cpt_match = 0
        for val in values:
            if val in frequency_list:
                indexFreq = frequency_list.index(val)
                raw_text += permutation[indexFreq]
        for word in word_dic:
            if word in raw_text:
                cpt_match+=1
        log = ""
        log += raw_text + "\n"
        log += str(cpt_match)+" matches for permutation "+ str(permutation)+"\n\n"
        print(log)
        if cpt_match >= best:
            fin = open("log.txt", "a", encoding='utf8')
            best = cpt_match
            fin.write(log)
            fin.close()
