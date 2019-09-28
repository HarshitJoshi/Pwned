import sys

def crack(psk, dictionary):
    with open(dictionary, 'r') as file:
        line_num = 0
        for line in file:
            if line.rstrip() == psk:
                return line, line_num
            line_num += 1
        return "psk not found in dict"

if __name__ == '__main__':
    dictionary=os.path.relpath("build_a_better_lock/words_alpha.txt")
    if len(sys.argv) > 1:
        dictionary = sys.argv[1]
    psk = input("Password: ")
    print(crack(psk, dictionary))
