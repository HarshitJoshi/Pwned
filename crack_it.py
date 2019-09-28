def crack(psk):
    with open('words_alpha.txt', 'r') as file:
        line_num = 0
        for line in file:
            if line.rstrip() == psk:
                return line, line_num
            line_num += 1
        return "psk not found in dict"

if __name__ == '__main__':
    psk = input("Password: ")
    print(crack(psk))
