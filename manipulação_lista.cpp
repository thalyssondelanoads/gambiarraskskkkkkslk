#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

#ifdef _WIN32
    #define CLEAR_SCREEN "cls"
#else
    #define CLEAR_SCREEN "clear"
#endif

void clean_screen() {
    std::system(CLEAR_SCREEN);
}

void show_menu() {
    std::cout << "-------------------------------\n"
              << "Remove a number - [ \033[31m1\033[m ]\n"
              << "Replace a number - [ \033[31m2\033[m ]\n"
              << "Add a number - [ \033[31m3\033[m ]\n"
              << "Arrange in ascending order - [ \033[31m4\033[m ]\n"
              << "Draw 1 random number from the list - [ \033[31m5\033[m ]\n"
              << "Show position of X elements in the list - [ \033[31m6\033[m ]\n"
              << "Clean screen - [ \033[31m7\033[m ]\n"
              << "End list manipulation - [ \033[31m0\033[m ]\n";
}

int main() {
    std::vector<int> list;
    int start, end;
    std::cout << "Enter the beginning and end of your list to create it :\n";
    std::cout << "Start : ";
    std::cin >> start;
    std::cout << "End : ";
    std::cin >> end;

    for (int i = start; i <= end; ++i) {
        list.push_back(i);
    }

    std::cout << "\033[32mList\033[m:\n\033[36m";
    for (int num : list) {
        std::cout << num << " ";
    }
    std::cout << "\033[m\n";

    show_menu();

    while (true) {
        int choice;
        std::cout << "Enter your option : ";
        std::cin >> choice;

        if (choice == 0) {
            std::cout << "\033[32mFinal List\033[m:\n\033[36m";
            for (int num : list) {
                std::cout << num << " ";
            }
            std::cout << "\033[m\n";
            break;
        } else {
            if (choice == 1) {
                int removed_number;
                std::cout << "Enter the number you want to remove : ";
                std::cin >> removed_number;
                list.erase(std::remove(list.begin(), list.end(), removed_number), list.end());
                std::cout << "\033[32mNew List\033[m:\n\033[36m";
                for (int num : list) {
                    std::cout << num << " ";
                }
                std::cout << "\033[m\n";
                show_menu();
            }

            // Implement other choices similarly
            // ...

            if (choice == 7) {
                clean_screen();
                std::cout << "\033[32mNew List\033[m:\n\033[36m";
                for (int num : list) {
                    std::cout << num << " ";
                }
                std::cout << "\033[m\n";
                show_menu();
            }
        }
    }

    return 0;
}