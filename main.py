from finnish_alphabet_frequency import finnish_alphabet_frequency
from utils import *
from noita_raw_text import *

# parse_all_data()


folders = ['Out/E1', 'Out/E2', 'Out/E3', 'Out/E4', 'Out/E5', 'Out/W1', 'Out/W2', 'Out/W3', 'Out/W4']

#Parse every folder
all_values = []
all_values_to_print = []
for folder in folders:
    print("Processing folder: "+folder+"\n")
    message = load_as_array(folder)
    pretty_print_message(message)
    trigrams = transform_to_trigram(message)
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
print()

#Get noita text list
print("Noita known words list")
noita_text_list = get_noita_text_as_list()
print(noita_text_list)
print()

#Get noita text frequency
print("Noita known words frequencies")
noita_frequency = compute_list_frequency(get_all_noita_text())
noita_frequency_sorted,noita_frequency_list = sort_dict(noita_frequency)
print(noita_frequency_sorted)  # {1: 1, 3: 4, 2: 9}
print(noita_frequency_list)
print()

noita_raw_frequency_list = [' ', 'I', 'A', 'T', 'U', 'N', 'L', 'E', 'O', 'S', 'K', 'Ä', 'M', 'J', '.', 'V', 'Y', 'R', 'P', 'H', 'D', ',', 'Ö', 'G']