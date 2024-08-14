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

def return_words(fin,qtd_letras):
    for line in fin:
        word = line.strip()
        formated_word = remove_space(word)
        if len(formated_word) > qtd_letras:
            print(formated_word)
        else:
            continue

    formated_word = remove_space(word)

    if len(formated_word) > qtd_letras:
        return formated_word

def return_words_with_letters_removed(fin):
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
                    
        if new_word != '':
            return new_word

def menu_design():
    return """
        ======== WORD-PLAY ========
[ 1 ] - PALAVRAS COM MAIS DE "X" LETRAS
[ 2 ] - PALAVRAS SEM "X" LETRA
[ 3 ] - LIMPAR TELA
[ 0 ] - SAIR
    """

def main():
    menu = menu_design()

    choice = 1
    while choice != 0:

        clean_screen()
        fin = open(str(input("""LOAD FILE: Informe o Arquivo [Ex: arquivo.txt]:
--> """)))
        print(menu)
        
        choice = int(input("Escolha a Opção: "))

        if choice == 1:
            option_1 = return_words(fin,qtd_letras)
            qtd_letras = int(input("Digite a Quantidade Mínima de Caracteres: "))
            print(option_1)
            
        if choice == 2:
            letter = str(input("Informe a Letra: "))
            option_2 = return_words_with_letters_removed(fin)
            print(option_2)
            
        if choice == 3:
            clean_screen()

main()
