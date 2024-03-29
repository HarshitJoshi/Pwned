import itertools
import json

# show output
debug = False 

# show dict output in json format
json_format = False

# change these values to your liking:
n = 3
m = 11

# DO NOT edit below this:
vowels = {
    "a":"a",
    "e":"e",
    "i":"i",
    "o":"o",
    "u":"u"
    }

pruning_steps = []

def gen_frequency():
    return {
            "a": 0, 
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0
    }


def gen_words(target_length):
    with open('words_alpha.txt', 'r') as file:
        line_num = 0
        words = []
        for line in file:
            word = line.rstrip()
            if len(word) == target_length and word[0] not in vowels:
                words.append(word)
        return words


def get_word_freq(words):
    frequency_table = []
    for i in range(0, n):
        frequency_table.append(gen_frequency())

    # get letter frequency
    for word in words:
        for i in range(0, n):
            frequency_table[i][word[i]] += 1
    return frequency_table


#
def gen_tumblers(frequency_table, words, m):
    tumblers = []

    for t in range(0, n):
        tumbler = []

        # get the most frequently used letters
        for i in range(0, m):
            freq_letter = max(frequency_table[t], key=frequency_table[t].get)
            tumbler.append(freq_letter)
            del frequency_table[t][freq_letter]
        tumblers.append(tumbler)
        
        # create a new list of words that contains the
        # most frequently used letter at the specified
        # position 't'
        pruned_words = []
        for word in words:
            if word[t] in tumblers[t]:
                pruned_words.append(word)
        if debug:
            print("Number of words from pruned words: {}".format(len(pruned_words)))
        pruning_steps.append(len(pruned_words))

        words = pruned_words

        # re-generate most frequently used letters list
        # from the 'pruned_words'
        frequency_table = get_word_freq(pruned_words)

        if debug:
            if json_format:
                print("Re-generated frequency table: {}\n".format(json.dumps(frequency_table, indent=2, sort_keys=True)))
            else:
                print("Re-generated frequency table: {}\n".format(frequency_table))
    return tumblers
    

def gen_combinations(tumblers):
    combinations = list(itertools.product(*tumblers))
    total_combinations = len(combinations)
    return combinations, total_combinations


if __name__ == '__main__':

    print("Running freq_chain/pruning algorithm...")
    words = gen_words(n)
    frequency_table = get_word_freq(words)
    num_valid_words = len(words)
    
    print("n(# of tumblers): {}\nm(# of letters in the tumblers): {}".format(n, m))
    print("Number of valid words of length(n) {}: {}".format(n, num_valid_words))
    
    if debug:
        for letter in frequency_table:
            if json_format:
                print("Frequency tables letters: {}".format(json.dumps(letter, indent=2, sort_keys=True)))
            else:
                print("Frequency tables letters: {}".format(letter))

    tumblers = gen_tumblers(frequency_table, words, m)
    if debug:
        print("Tumblers:")
        for tumbler in tumblers:
            print(tumbler)
        print()
    combinations, total_combinations = gen_combinations(tumblers)
    
    # count how many combinations are in the dict
    count = 0
    for letter_tuple in combinations:
        word = ''.join(letter_tuple)
        if word in words:
            count += 1
    
    print("Pruning steps: ")
    for step in pruning_steps:
        print(step)
    print("Matching combinations: {}".format(count))
    print("Total combinations: {}".format(total_combinations))
    print("Percentage of matching/valid_words: {}".format(count/num_valid_words))
    print("Percentage of matching/total_combinations: {}".format(count/total_combinations))
    
