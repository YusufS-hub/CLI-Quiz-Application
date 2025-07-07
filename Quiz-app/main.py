import anime
import hxheasy
import hxhmedium
import hxhhard
import hajimehard
import Onepiecehard
import os


# Clear The Terminal Function
def clear_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
# Appication Banner
print(r'''
  ___  _   _ ___ _____
 / _ \| | | |_ _|__  /
| | | | | | || |  / / 
| |_| | |_| || | / /_ 
 \__\_\\___/|___/____|
 
WELCOME TO THE QUIZ! 
''')

# Main Menu for Quizzes
def main_menu():
    print(r"+----------------------------+")
    print(r"|      Main Quiz Menu        |")
    print(r"+----------------------------+")
    print(r"| 0 - Exit Application       |")
    print(r"| 1 - Anime Quizzes          |")
    print(r"| 2 - Video Game Quizzes     |")
    print(r"| 3 - TV Show Quizzes        |")
    print(r"+----------------------------+")





def main():
    while True:
        main_menu()
        try:
            main_menu_option = int(input('Enter a number corresponding to what option you would like (0-3): '))
            if main_menu_option == 0:
                print('Exiting App ...')
                print('Goodbye!')
                quit()
            elif main_menu_option == 1:
                clear_menu()
                while True:
                    anime.quizzes()
                    anime_menu_option = int(input('Enter a number corresponding to what option you would like (0-4): '))
                    if anime_menu_option == 0:
                        print('You Have Returned To The Main Menu')
                        break
                    elif anime_menu_option == 1:
                        clear_menu()
                        while True:
                            anime.difficulty_hxh()
                            hxh_option = int(input('Enter a number corresponding to what option you would like (0-3): '))
                            if hxh_option == 0:
                                clear_menu()
                                print('You Have Returned To The Anime Menu')
                                break
                            elif hxh_option == 1:
                                clear_menu()
                                print('You Have Began The HXH Easy Quiz')
                                hxheasy.question1()
                                hxheasy.question2()
                                hxheasy.question3()
                                hxheasy.question4()
                                hxheasy.question5()
                                hxheasy.all_points()
                            elif hxh_option == 2:
                                clear_menu()
                                hxhmedium.question1()
                                hxhmedium.question2()
                                hxhmedium.question3()
                                hxhmedium.question4()
                                hxhmedium.question5()
                                hxhmedium.all_points()
                            elif hxh_option == 3:
                                clear_menu()
                                hxhhard.question1()
                                hxhhard.question2()
                                hxhhard.question3()
                                hxhhard.question4()
                                hxhhard.question5()
                                hxhhard.all_points()
                    elif anime_menu_option == 2:
                        clear_menu()
                        while True:
                            anime.difficulty_hajime()
                            hajime_option = int(input('Enter a number corresponding to what option you would like (0-3): '))
                            if hajime_option == 0:
                                clear_menu()
                                print('You Have Returned To The Anime Menu')
                                break
                            elif hajime_option == 1:
                                clear_menu()
                                print('No Easy For this Anime')
                                break
                            elif hajime_option == 2:
                                print('No Medium For this Anime')
                                break
                            elif hajime_option == 3:
                                clear_menu()
                                hajimehard.question1()
                                hajimehard.question2()
                                hajimehard.question3()
                                hajimehard.question4()
                                hajimehard.question5()
                                hajimehard.all_points()
                    elif anime_menu_option == 3:
                        clear_menu()
                        while True:
                            anime.difficulty_Onepiece()
                            one_option = int(input('Enter a number corresponding to what option you would like (0-3): '))
                            if one_option == 0:
                                clear_menu()
                                print('You Have Returned To The Anime Menu')
                                break
                            elif one_option == 1:
                                clear_menu()
                                print('No Easy For this Anime')
                                break
                            elif one_option == 2:
                                print('No Medium For this Anime')
                                break
                            elif one_option == 3:
                                clear_menu()
                                Onepiecehard.question1()
                                Onepiecehard.question2()
                                Onepiecehard.question3()
                                Onepiecehard.question4()
                                Onepiecehard.question5()
                                Onepiecehard.all_points()
                               
        except (ValueError, UnboundLocalError):
            print('Invalid Input Enter numbers (0-3)')
main()