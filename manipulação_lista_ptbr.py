def limpar_tela():
  import os
  os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
  menu = '''-------------------------------        
Remover um número - [ \033[31m1\033[m ]
Substituir um número - [ \033[31m2\033[m ]
Adicionar um número - [ \033[31m3\033[m ]
Organizar em ordem crescente - [ \033[31m4\033[m ]
Sortear 1 número aleatório da lista - [ \033[31m5\033[m ]
Mostrar a posição de X elementos na lista - [ \033[31m6\033[m ]
Limpar tela - [ \033[31m7\033[m ]
Finalizar manipulação de lista - [ \033[31m0\033[m ]
'''
  print(menu)

def main():
  import random

  print('Digite o início e o fim da sua lista para criá-la:')
  inicio = int(input('Início : '))
  final = int(input('Final : '))

  inserir_numero = inicio
  lista = []
  for inserir_numero in range (inicio,final+1):
    lista.append(inserir_numero)
  print(f'\033[32mLista\033[m:\n\033[36m{lista}\033[m')

  mostrar_menu()

  while True:
      opçao = int(input('Digite sua opção : '))

      if opçao == 0:
          print(f'\033[32mLista Final\033[m:\n\033[36m{lista}\033[m')
          break

      else:
          if opçao == 1:
            remover_numero = int(input('Digite o número que deseja remover : '))
            del lista[lista.index(remover_numero)]
            print(f'\033[32mNova Lista\033[m:\n\033[36m{lista}\033[m')
            mostrar_menu()

          if opçao == 2:
            substituir_numero = int(input('Digite o número que deseja substituir : '))
            novo_numero = int(input('Digite o número que deseja inserir no local : '))
            lista[lista.index(substituir_numero)] = novo_numero
            print(f'\033[32mNova Lista\033[m:\n\033[36m{lista}\033[m')
            mostrar_menu()

          if opçao == 3:
            adicionar_numero = int(input('Digite o número que deseja adicionar : '))
            lista.append(adicionar_numero)
            print(f'\033[32mNova Lista\033[m:\n\033[36m{lista}\033[m')
            mostrar_menu()

          if opçao == 4:
            lista = sorted(lista)
            print(f'\033[32mNova Lista\033[m:\n\033[36m{lista}\033[m')
            mostrar_menu()

          if opçao == 5:
            seleçao_aleatoria = random.choice(lista)
            print('\033[33mO número sorteado foi\033[m : ',seleçao_aleatoria)
            mostrar_menu()

          if opçao == 6:
            posiçao = int(input('Digite quais primeiras posições você deseja ver (Digite "0" se quiser ver todas) : '))
            if posiçao != 0:
              for pos,numeros in enumerate(lista[:posiçao]):
                print(f'\033[35m{pos}º Posição\033[m -> \033[32m{numeros}\033[m')
              mostrar_menu()
            else:
              for pos,numeros in enumerate(lista):
                print(f'\033[35m{pos}º Posição\033[m -> \033[32m{numeros}\033[m')
              mostrar_menu()

          if opçao == 7:
            limpar_tela()
            print(f'\033[32mNova Lista\033[m:\n\033[36m{lista}\033[m')
            mostrar_menu()

if __name__ == "__main__":
  main()
