from natsort import natsorted, ns
import os
from numpy import random
import numpy as np

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

            trigrams_line.append([message[i][j], message[i + 1][j], message[i][j + 1]])
            if j + 2 < len(message[i]):
                trigrams_line.append([message[i + 1][j + 2], message[i][j + 2], message[i + 1][j + 1]])
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
most_frequent_finnish_letters = ['I', 'A', 'T', 'S', 'E', 'U', 'K', 'N', 'L', 'O', 'R', 'Ä', 'P', 'M', 'V', 'H', 'Y', 'J', 'D', 'Ö', 'G', 'F', 'B', 'C', 'W', 'Z', 'Š', 'X', 'Q', 'É', 'Ž']

def test_permutation(values,frequency_list,permutation,word_dic,show_text):
    raw_text = ""
    cpt_match = 0
    list_word = []
    for val in values:
        if val in frequency_list:
            indexFreq = frequency_list.index(val)
            raw_text += permutation[indexFreq]
        else:
            pass
            raw_text += "\n"

    for word in word_dic:
        if word in raw_text:
            list_word.append(word)
            cpt_match += 1

    if show_text == True:
        print(raw_text)
    print("Word match number : " + str(cpt_match)+" "+str(list_word))
    return raw_text

def do_random_permutations(values,frequency_list,permutation,word_dic,n = 10000):
    best = 0
    for i in range(n):
        word_list = []
        random.shuffle(permutation)
        raw_text = ""
        cpt_match = 0
        for val in values:
            if val in frequency_list:
                indexFreq = frequency_list.index(val)
                raw_text += permutation[indexFreq]
        for word in word_dic:
            if word in raw_text:
                word_list.append(word)
                cpt_match+=1
        log = ""
        log += raw_text + "\n"
        log += str(word_list)
        log += str(cpt_match)+" matches for permutation "+ str(permutation)+"\n\n"
        print(log)
        if cpt_match >= best:
            fin = open("log.txt", "a", encoding='utf8')
            best = cpt_match
            fin.write(log)
            fin.close()

def run_explorator_cli(values,frequency_list,word_dic):
    permutation_1 = ['A', 'I', 'T', 'N', 'E', 'S', 'O', 'L', 'Ä', 'K', 'U', 'M', 'H', 'V', 'R', 'J', 'P', 'Y', 'D', 'Ö', 'G', 'C', 'B', 'F', 'W', 'Z', 'X', 'Å', 'Q', 'Š', 'Ž', '.', ',', ' ']
    change_letter_1 = ""
    change_letter_2 = ""
    permutation_dyn = permutation_1
    test_permutation(values,frequency_list,permutation_dyn,word_dic,show_text=True)
    while change_letter_1.upper() is not "STOP":
        print("current permutation : "+str(permutation_dyn))
        change_letter_1 = input("choose letter 1 or stop to quit\n")
        #if change_letter_1 not in permutation_dyn:
        #    print("selected letter ",change_letter_1," doesn't exist in current permutation")
        #    continue
        if change_letter_1.upper() is not "STOP":
            change_letter_2 = input("choose letter 2\n")
            #if change_letter_2 not in permutation_dyn:
            #    print("selected letter ",change_letter_2," doesn't exist in current permutation")
            #    continue
            if len(change_letter_2) != len(change_letter_1):
                print("key size doesn't match")
                continue
            unique_chage = {}
            for i in range(len(change_letter_1)):
                l1 = change_letter_1[i]
                l2 = change_letter_2[i]
                if l1 not in unique_chage:
                    unique_chage[l2] = l1
                    unique_chage[l1] = l2
                else:
                    l1 = unique_chage[l1]
                index_1 = permutation_dyn.index(l1)
                index_2 = permutation_dyn.index(l2)

                print(permutation_dyn[index_1] + " > "+permutation_dyn[index_2])

                permutation_dyn[index_1] = l2
                permutation_dyn[index_2] = l1


            print("new permutation : " + str(permutation_dyn))
            input("Press enter to process")
            test_permutation(values, frequency_list, permutation_dyn, word_dic, show_text=True)

def shift_right(val_array):
    val_list = val_array.tolist()
    val_list.pop()
    val_list.insert(0, 0)
    return np.array(val_list)

def match_string(list_a, list_b):
    match = []
    for i in range(len(list_a)) :
        if list_a[i] == list_b[i] and list_b[i] != '0':
            match.append(list_b[i])
        else:
            match.append(' ')
    return " ".join(''.join(match).split())


def find_matching_patterns(text,size_limit):
    words = []
    text_array = np.array(list(text))
    padding = np.full(text_array.shape,' ')
    padded_text = np.concatenate((text_array, padding, padding))
    key = np.concatenate((text_array, padding, padding))

    loop_len = int(len(key)/3)*2
    for i in range(loop_len):
        padded_text = shift_right(padded_text)
        res = match_string(key,padded_text)
        for word in res.split(' '):
            if len(word) >= size_limit:
                words.append(word)
    return catch_unique(words)