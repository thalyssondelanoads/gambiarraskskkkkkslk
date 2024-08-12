def remove_space(word):
    new_word = ''

    for character in word:

        if character != ' ':
            new_word += character
        else:
            continue

    return new_word



def main():
    fin = open('words.txt')

    for line in fin:
        word = line.strip()

        formated_word = remove_space(word)

        if len(formated_word) > 20:
            print(formated_word)


main()
