def clean_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def remove_space(word):
    new_word = ''

    for character in word:

        if character != ' ':
            new_word += character
        else:
            continue

    return new_word


def option_2(word):

    formated_word = remove_space(word)

    if len(formated_word) > 20:
        return formated_word


def menu_design():
    return """
        ======== WORD-PLAY ========
[ 1 ] - LOAD FILE
[ 2 ] - PALAVRAS COM MAIS DE 20 LETRAS
[ 3 ] - PALAVRAS SEM "X" LETRA
[ 4 ] - PALAVRAS COM MAIS DE "X" LETRAS
[ 0 ] - SAIR
    """

def main():
    #Exibição do menu
    menu = menu_design()

    choice = 1

    while choice != 0:

        clean_screen()
        print(menu)

        choice = int(input("Escolha a Opção: "))

        if choice == 1:
            fin = open(str(input('''Informe o Arquivo [Ex: arquivo.txt]
:''')))
        elif choice == 2: #pfv funcione
            for line in fin:
                word = line.strip()

                formated_word = remove_space(word)

                if len(formated_word) > 20:
                    print(formated_word)
                else:
                    continue
        
        elif choice == 3:
            letter = str(input('Informe a Letra: '))
            
            for line in fin:
                word = line.strip()

                formated_word = remove_space(word)

                new_word = ''
                for character in formated_word:
                    
                    if character == letter:
                        break
                    else:
                        new_word += character
                
                #gambiarra das grandes kkk
                if new_word != '':
                    print(new_word)
        
        elif choice == 4:
            X = int(input("Digite a Quantidade de Letras das Palavras: "))
            for line in fin:
                word = line.strip()

                formated_word = remove_space(word)

                if len(formated_word) > X:
                    print(formated_word)
                else:
                    continue


        clear = input('\033[32mPRESSIONE ENTER\033[m')


main()
