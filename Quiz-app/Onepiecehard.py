points = 0
def reset_points():
    global points 
    points = 0

def question1():
    reset_points()
    global points
    print('Starting Hard One Piece Quiz !')
    print('The 1st Question Is \nWhat was the name of the priest (vassal) who fought Chopper during the Skypiea arc?')
    print(r"+------------------------+")
    print(r"| a - Ohm                |")
    print(r"| b - Gedatsu            |")
    print(r"| c - Shura              |")
    print(r"+------------------------+")

    while True:
        answer = input('Enter Your Answer a, b or c: ')
        if answer != 'a' and answer != 'b' and answer != 'c':
            print('Enter a, b or c ! ')
            continue
        elif answer == 'a':
            print('Incorrect!')
            break
        elif answer == 'b':
            print('Incorrect!')
            break
        elif answer == 'c':
            print('Correct! 1 point')
            points += 1
            break
    print('\n')  
      
def question2():
    global points
    print('The 2nd Question Is \nWhat unique feature distinguishes Admiral Kizarus speech style in the anime?')
    print(r"+------------------------------------------------+")
    print(r"| a - He stretches his words slowly              |")
    print(r"| b - He ends most sentences with 'yo'           |")
    print(r"| c - He pauses and laughs mid-sentence          |")
    print(r"+------------------------------------------------+")

    while True:  
        answer = input('Enter Your Answer a, b or c: ')
        if answer != 'a' and answer != 'b' and answer != 'c':
            print('Enter a, b or c ! ')
            continue
        elif answer == 'a':
            print('Correct! 1 point')
            points += 1
            break
        elif answer == 'b':
            print('Incorrect!')
            break
        elif answer == 'c':
            print('Incorrect!')
            break
    print('\n')
    
def question3():
    global points
    print('The 3rd Question Is \nWhat is the exact Japanese kanji written on the back of Vice Admiral Garps dog mask helmet?')
    print(r"+----------------------------+")
    print(r"| a - 正義 (Justice)          |")
    print(r"| b -  犬 (Dog)               |")
    print(r"| c - 中将 (Vice Admiral)     |")
    print(r"+----------------------------+")

    while True: 
        answer = input('Enter Your Answer a, b or c: ')
        if answer != 'a' and answer != 'b' and answer != 'c':
            print('Enter a, b or c ! ')
            continue 
        elif answer == 'a':
            print('Incorrect!')
            break
        elif answer == 'b':
            print('Correct! 1 point')
            points += 1
            break
        elif answer == 'c':
            print('Incorrect!')
            break
    print('\n')


def question4():
    global points
    print('The 4th Question Is \nIn the anime, what color are Robins eyes in her first appearance as Miss All Sunday aboard Crocodiles ship?')
    print(r"+------------------+")
    print(r"| a - Blue         |")
    print(r"| b - Brown        |")
    print(r"| c - Green        |")
    print(r"+------------------+")

    while True: 
        answer = input('Enter Your Answer a, b or c: ')
        if answer != 'a' and answer != 'b' and answer != 'c':
            print('Enter a, b or c ! ')
            continue 
        elif answer == 'a':
            print('Incorrect!')
            break
        elif answer == 'b':
            print('Incorrect!')
            points += 1
            break
        elif answer == 'c':
            print('Correct! 1 point')
            points += 1
            break
    print('\n')


def question5():
    global points
    print('The Final Question Is \nWhat is the name of the island that Luffy mistakes for a “giant cake” when the Straw Hats are falling from Skypeia?')
    print(r"+--------------------------------+")
    print(r"| a - Long Ring Long Land        |")
    print(r"| b - Jaya                       |")
    print(r"| c - Navarone                   |")
    print(r"+--------------------------------+")

    while True: 
        answer = input('Enter Your Answer a, b or c: ')
        if answer != 'a' and answer != 'b' and answer != 'c':
            print('Enter a, b or c ! ')
            continue 
        elif answer == 'a':
            print('Incorrect!')
            points += 1
            break
        elif answer == 'b':
            print('Incorrect!')
            break
        elif answer == 'c':
            print('Correct! 1 point')
            points += 1
            break
    print('\n')


def all_points():
    print(f'You got {points} out of 5 for the One Piece Quiz!')