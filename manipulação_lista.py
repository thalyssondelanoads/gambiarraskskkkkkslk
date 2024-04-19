def clean_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
  
def show_menu():
    menu = '''-------------------------------        
Remove a number - [ \033[31m1\033[m ]
Replace a number - [ \033[31m2\033[m ]
Add a number - [ \033[31m3\033[m ]
Arrange in ascending order - [ \033[31m4\033[m ]
Draw 1 random number from the list [ \033[31m5\033[m ]
Show position of X elements in the list [ \033[31m6\033[m ]
Clean screen [ \033[31m7\033[m ]
End list manipulation [ \033[31m0\033[m ]
'''
    print(menu)

def main():
    import random
    
    print('Enter the beginning and end of your list to create it :')
    start = int(input('Start : '))
    end = int(input('End : '))

    insert_number = start
    list = []
    for insert_number in range (start,end+1):
      list.append(insert_number)
    print(f'\033[32mList\033[m:\n\033[36m{list}\033[m')

    show_menu()

    while True:
        choice = int(input('Enter your option : '))
        
        if choice == 0:
            print(f'\033[32mFinal List\033[m:\n\033[36m{list}\033[m')
            break
        
        else:
            if choice == 1:
              removed_number = int(input('Enter the number you want to remove : '))
              del list[list.index(removed_number)]
              print(f'\033[32mNew List\033[m:\n\033[36m{list}\033[m')
              show_menu()
            
            if choice == 2:
              replaced_number = int(input('What number do you want to replace : '))
              new_number = int(input('What number do you want to add instead : '))
              list[list.index(replaced_number)] = new_number
              print(f'\033[32mNew List\033[m:\n\033[36m{list}\033[m')
              show_menu()
            
            if choice == 3:
              add_number = int(input('What number do you want to add : '))
              list.append(add_number)
              print(f'\033[32mNew List\033[m:\n\033[36m{list}\033[m')
              show_menu()
            
            if choice == 4:
              list = sorted(list)
              print(f'\033[32mNew List\033[m:\n\033[36m{list}\033[m')
              show_menu()
            
            if choice == 5:
              random_selection = random.choice(list)
              print('\033[33mThe number drawn was\033[m : ',random_selection)
              show_menu()
            
            if choice == 6:
              positions = int(input('Enter which top positions you want to see (Type "0" if you want to see everyone) : '))
              
              if positions != 0:
                for pos,numbers in enumerate(list[:positions]):
                  print(f'\033[35m{pos}º Position\033[m -> \033[32m{numbers}\033[m')
                show_menu()
              else:
                for pos,numbers in enumerate(list):
                  print(f'\033[35m{pos}º Position\033[m -> \033[32m{numbers}\033[m')
                show_menu()
            
            if choice == 7:
              clean_screen()
              print(f'\033[32mNew List\033[m:\n\033[36m{list}\033[m')
              show_menu()

if __name__ == "__main__":
    main()
