from finnish_alphabet_frequency import finnish_alphabet_frequency
from utils import *
from noita_raw_text import *
import numpy as np

from scipy.ndimage.interpolation import shift
from view import create_main_view

#create_main_view()

# parse_all_data()

import cv2
# parse_all_data()

"""
folders = ['Out/east_1', 'Out/east_2', 'Out/east_3', 'Out/east_4', 'Out/east_5', 'Out/west_1', 'Out/west_2', 'Out/west_3', 'Out/west_4']

#Parse every folder
all_values = []
all_values_to_print = []
all_trigrams = []

for folder in folders:
    print("Processing folder: "+folder+"\n")
    message = load_as_array(folder)
    pretty_print_message(message)
    trigrams = transform_to_trigram(message)
    for line in trigrams:
        for trigram in line:
            all_trigrams.append(trigram)
    pretty_print_trigrams(trigrams)
    values = parse_trigrams_to_numeric(trigrams)
    pretty_print_values(values)

    for lines in values:
        all_values_to_print.append(lines)

        for value in lines:
            all_values.append(value)
        all_values.append("\n")
    #Each message is ended by a white space
    all_values.append("\n")
    all_values_to_print.append(["\n"])

all_values_no_whitespace = []
for value in all_values:
    if value is not '\n':
        all_values_no_whitespace.append(value)

#find text patterns

#Print everything for convenience
#pretty_print_values(all_values_to_print)

#Print all values
print("All values :")
print(all_values_no_whitespace)
print()

unique_trigrams = catch_unique(all_values_no_whitespace)
print("Number of unique trigram :")
print(len(unique_trigrams))
print()

#Compute all values frequency
print("All values frequency")
frequency = compute_list_frequency(all_values_no_whitespace)
frequency_sorted,frequency_list = sort_dict(frequency)
print(frequency_sorted)  # {1: 1, 3: 4, 2: 9}
print(frequency_list)  # {1: 1, 3: 4, 2: 9}
print()

#Get noita text list
print("Noita known words list")
noita_text_list = get_noita_text_as_list()
noita_text_list_unique = catch_unique(noita_text_list)
print(noita_text_list_unique)
print()

#Get noita text list frequency
print("Noita known words frequency")
noita_text_list_frequency = compute_list_frequency(noita_text_list)
noita_text_list_frequency_sorted,noita_text_list_frequency_list = sort_dict(noita_text_list_frequency)
print(noita_text_list_frequency_sorted)  # {1: 1, 3: 4, 2: 9}
print(noita_text_list_frequency_list)  # {1: 1, 3: 4, 2: 9}
sorted_word_list = noita_text_list_frequency_list.copy()
sorted_word_list.sort()
print("ordered word list",str(sorted_word_list))
print()


#Get noita text frequency
print("Noita known words letter frequencies")
noita_frequency = compute_list_frequency(get_all_noita_text())
noita_frequency_sorted,noita_frequency_list = sort_dict(noita_frequency)
print(noita_frequency_sorted)  # {1: 1, 3: 4, 2: 9}
print(noita_frequency_list)
print("noita char count : "+str(len(noita_frequency_list)))
print()

#Used to test manual permutation to find word matches
noita_raw_frequency_list = [' ', 'I', 'A', 'T', 'U', 'N', 'L', 'E', 'O', 'S', 'K', '??', 'M', 'J', '.', 'V', 'Y', 'R', 'P', 'H', 'D', ',', '??', 'G']

#for letter in most_frequent_finnish_letters:
#    if letter not in noita_raw_frequency_list:
#        noita_raw_frequency_list.append(letter)
#print(noita_raw_frequency_list)

raw_permutation = [' ', 'I', 'A', 'T', 'U', 'N', 'L', 'E', 'O', 'S', 'K', '??', 'M', 'J', '.', 'V', 'Y', 'R', 'P', 'H', 'D', ',', '??', 'G', 'C', 'B', 'F', 'W', 'Z', 'X', '??', 'Q', '??', '??']

#do_random_permutations(all_values,frequency_list,permutation_3,noita_text_list_unique,1000000)
permutation_1 = ['A', 'I', 'T', 'N', 'E', 'S', 'O', 'L', '??', 'K', 'U', 'M', 'H', 'V', 'R', 'J', 'P', 'Y', 'D', '??','G', 'C', 'B', 'F', 'W', 'Z', 'X', '??', 'Q', '??', '??', '.', ',', ' ']

permutation_dyn = permutation_1
raw_text = test_permutation(all_values, frequency_list, permutation_dyn, noita_text_list_unique, show_text=False)


#matches = find_matching_patterns(raw_text,4)
#matches.sort()
#print(matches)

matches = ['IEBKN', 'IEBKNHVSA', 'IEBKNHVSAHOSKL??XKPEL', 'IEJFTKSQMINIFPNRAK??HSTBE', 'NSNLJJIUJTLUB', 'RSU??']

#run_explorator_cli(all_values,frequency_list,noita_text_list_unique)


print(raw_text)
print(len(catch_unique(all_trigrams)))

mega_dic = get_finish_dict()

def all_different(pattern):
    if len(pattern) == len(set(pattern)):
        return True
    else:
        return False


match = {}
for word in mega_dic:
    pattern = word[1:6]
    if pattern not in match.keys():
        match[pattern] = []
    if all_different(pattern) == True and len(word) >= 6:
        match[pattern].append(word)

def nb_diff_letter(list):
    first_letter_list = []
    for word in list:
        if word[0] not in first_letter_list:
            first_letter_list.append(word[0])

    return len(first_letter_list)

for key in match:
    if nb_diff_letter(match[key]) >= 6:
        print(key)
        for word in match[key]:
            print("\t"+word)
"""

C_array = np.array(cv2.imread('Data/MinimalPattern/C.png',cv2.IMREAD_GRAYSCALE))
N_array = np.array(cv2.imread('Data/MinimalPattern/N.png',cv2.IMREAD_GRAYSCALE))
S_array = np.array(cv2.imread('Data/MinimalPattern/S.png',cv2.IMREAD_GRAYSCALE))
E_array = np.array(cv2.imread('Data/MinimalPattern/E.png',cv2.IMREAD_GRAYSCALE))
W_array = np.array(cv2.imread('Data/MinimalPattern/W.png',cv2.IMREAD_GRAYSCALE))

print(N_array)
message = parse_message_as_array(load_as_array('Out/east_1'))

def copy_black_pixel(image,template):
    for i in range(4):
        for j in range(4):
            if template[i][j] == 0:
                image[i][j] = 0
    return image

cpt_i = 0
cpt_j = 0
i = 0
j = 0
offset = 4
pixel_size = 4
image = np.full((len(message)*5,len(message[0])*5),255)

print(len(message))
while i < len(message):
    while j < len(message[i]):
        cpt_i = i*offset
        cpt_j = j*offset
        if i%2 == 1:
            cpt_j+=int(pixel_size/2)
        eye_code = message[i][j]
        print(eye_code)
        if eye_code == 'C':
            copy_black_pixel(image[cpt_i:cpt_i+pixel_size,cpt_j:cpt_j+pixel_size], C_array)
        if eye_code == 'N':
            copy_black_pixel(image[cpt_i:cpt_i+pixel_size,cpt_j:cpt_j+pixel_size], N_array)
        if eye_code == 'S':
            copy_black_pixel(image[cpt_i:cpt_i+pixel_size,cpt_j:cpt_j+pixel_size], S_array)
        if eye_code == 'E':
            copy_black_pixel(image[cpt_i:cpt_i+pixel_size,cpt_j:cpt_j+pixel_size], E_array)
        if eye_code == 'W':
            copy_black_pixel(image[cpt_i:cpt_i+pixel_size,cpt_j:cpt_j+pixel_size], W_array)
        j += 1

    i += 1
    j = 0

cv2.imwrite("TEST3" + ".png", image)

