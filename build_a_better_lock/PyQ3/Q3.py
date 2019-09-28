from string import ascii_lowercase
import time
from itertools import permutations
from itertools import product
import trie


def tumblers_recursively(counter=0, k=0, count=0):
    global maxc, amax, start
    if counter == int(tumblers) - 1:
        for i in range(len(list(permutations(ascii_lowercase, int(set_of_characters))))):
            for j in range(int(set_of_characters)):
                perm = permutations(ascii_lowercase, int(set_of_characters))
                a[counter][j] = list(perm)[i][j]
            # print(a)
            # print(list(product(*a)))
            for x in list(product(*a)):
                # print("".join(x))
                for strings in root.get_possible_words(''.join(x)):
                    # print("word: {}".format(word))
                    if strings == ''.join(x):
                        count = count + 1
                        # print(''.join(x))
            # print("count: {}".format(count))
            if count > maxc:
                maxc = count
                amax = a
                print("\nMAX TUMBLERS: {}".format(amax))
                print("Max combination: {}".format(maxc))
                for x in list(product(*a)):
                    # print("".join(x))
                    for strings in root.get_possible_words(''.join(x)):
                        # print("word: {}".format(word))
                        if strings == ''.join(x):
                            print(''.join(x), end=' ')
            if maxc == int(pow(int(set_of_characters), int(tumblers))):
                end = time.time()
                print("\n", end - start)
                print("\nALL DONE")
                exit(0)
            count = 0
    else:
        while k != len(list(permutations(ascii_lowercase, int(set_of_characters)))):
            for j in range(int(set_of_characters)):
                perm = permutations(ascii_lowercase, int(set_of_characters))
                a[counter][j] = list(perm)[k][j]
            tumblers_recursively(counter + 1, k, count)
            k += 1


if __name__ == "__main__":
    print("Loading trie...")
    f = open("text.txt", "r")
    root = trie.Trie()
    for word in f:
        root.insert(word)
    tumblers = input("Enter n: ")
    set_of_characters = input("Enter m: ")

    maxc = 0
    a = [[0 for i in range(int(set_of_characters))] for j in range(int(tumblers))]
    amax = [[0 for i in range(int(set_of_characters))] for j in range(int(tumblers))]
    maxlist = []

    start = time.time()
    tumblers_recursively()
