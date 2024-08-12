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

        new_word = ''
        for character in formated_word:
            
            if character == 'e':
                break
            else:
                new_word += character
        
        #gambiarra das grandes kkk
        if new_word != '':
            print(new_word)


main()
