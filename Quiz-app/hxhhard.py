points = 0

def reset_points():
    global points 
    points = 0

def question1():
    reset_points()
    global points
    print('The 1st Question Is \nIn the Hunter Exam arc, which applicant number did Killua have?')
    print(r"+----------------------------+")
    print(r"| a - 44                     |")
    print(r"| b - 405                    |")
    print(r"| c - 99                     |")
    print(r"+----------------------------+")

    while True:
        answer = input('Enter Your Answer a, b or c: ').lower()
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
    print('The 2nd Question Is \nDuring the dodgeball game on Greed Island, what position did Killua play?')
    print(r"+----------------------------+")
    print(r"| a - Passer                 |")
    print(r"| b - Receiver               |")
    print(r"| c - Thrower                |")
    print(r"+----------------------------+")

    while True:  
        answer = input('Enter Your Answer a, b or c: ').lower()
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
    
def question3():
    global points
    print('The 3rd Question Is \nWhat is the exact phrase Biscuit uses to introduce herself when she first meets Gon and Killua?')
    print(r"+-------------------------------------------------------------+")
    print(r"| a - “My names Biscuit, but call me Bisky!”                  |")
    print(r"| b - “You can call me Bisky, short for Biscuit Krueger.”     |")
    print(r"| c - “My name is Biscuit Krueger. Pleased to meet you.”      |")
    print(r"+-------------------------------------------------------------+")

    while True: 
        answer = input('Enter Your Answer a, b or c: ').lower()
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


def question4():
    global points
    print('The 4th Question Is \nIn the Phantom Troupe arc, which Spider number is Machi?')
    print(r"+-------------------+")
    print(r"| a - 4             |")
    print(r"| b - 6             |")
    print(r"| c - 3             |")
    print(r"+-------------------+")

    while True: 
        answer = input('Enter Your Answer a, b or c: ').lower()
        if answer != 'a' and answer != 'b' and answer != 'c':
            print('Enter a, b or c ! ')
            continue 
        elif answer == 'a':
            print('Incorrect!')
            points += 1
            break
        elif answer == 'b':
            print('Correct! 1 point')
            points += 1
            break
        elif answer == 'c':
            print('Incorrect!')
            break
    print('\n')


def question5():
    global points
    print('The Final Question Is \nWhat was the first Greed Island spell card Gon successfully used during gameplay?')
    print(r"+-----------------------+")
    print(r"| a - Book              |")
    print(r"| b - Gain              |")
    print(r"| c - Accompany         |")
    print(r"+-----------------------+")

    while True: 
        answer = input('Enter Your Answer a, b or c: ').lower()
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


def all_points():
    print(f'You got {points} out of 5 for the Easy HxH Quiz!')