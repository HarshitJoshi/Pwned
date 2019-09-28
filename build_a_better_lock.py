import itertools

debug = False

n = 3
m = 26

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
            if len(word) == target_length:
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


# generate the tumblers' letters based on the most
# frequently occurred letter of the words in the dict 
def gen_tumblers(frequency_table, m):
    tumblers = []
    # get top 'm' most frequent letters
    for frequency_list in frequency_table:
        tumbler = []
        for i in range(0, m):
            freq_letter = max(frequency_list, key=frequency_list.get)
            print(freq_letter, end="")
            #tumblers[i].append(freq_letter)
            tumbler.append(freq_letter)
            del frequency_list[freq_letter]
        tumblers.append(tumbler)
        print()
    return tumblers

def gen_combinations(tumblers):
    combinations = list(itertools.product(*tumblers))
    total_combinations = len(combinations)
    return combinations, total_combinations


if __name__ == '__main__':
    words = gen_words(n)
    frequency_table = get_word_freq(words)
    
    if debug:
        for letter in frequency_table:
            print(letter)

    tumblers = gen_tumblers(frequency_table, m)
    combinations, total_combinations = gen_combinations(tumblers)
    
    # count how many combinations are in the dict
    count = 0
    for letter_tuple in combinations:
        word = ''.join(letter_tuple)
        print(word)
        if word in words:
            count += 1

    print(count)
    print("Accuracy of matching combinations: {} by total combinations: {} is: {}".format(count, total_combinations, count/total_combinations))
