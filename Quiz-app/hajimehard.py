points = 0
def reset_points():
    global points 
    points = 0

def question1():
    reset_points()
    global points
    print('Starting Hard Hajime No Ippo Quiz !')
    print('The 1st Question Is \nWhat unusual item does Takamura keep in his locker as a “good luck charm”?')
    print(r"+----------------------------===========+")
    print(r"| a - A gravure magazine                |")
    print(r"| b - A lucky coin                      |")
    print(r"| c - A picture of himself flexing      |")
    print(r"+---------------------------------------+")

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
    print('The 2nd Question Is \nWhich of these opponents did Ippo defeat with a counter punch instead of pressure fighting?')
    print(r"+----------------------------+")
    print(r"| a - Kobashi               |")
    print(r"| b - Sanada                 |")
    print(r"| c - Hayami                |")
    print(r"+----------------------------+")

    while True:  
        answer = input('Enter Your Answer a, b or c: ').lower()
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
    print('The 3rd Question Is \nWhat food does Ippo bring Takamura to thank him after their first training session?')
    print(r"+----------------------------+")
    print(r"| a - Rice balls             |")
    print(r"| b - Mackerel               |")
    print(r"| c - Bento box              |")
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


def question4():
    global points
    print('The 4th Question Is \nWhat did Ippo write on his application form to become a pro boxer under "Reason for joining"?')
    print(r"+------------------------------------------------+")
    print(r"| a - To become strong                           |")
    print(r"| b - To find out what it means to be strong.    |")
    print(r"| c - To protect the people I care about.        |")
    print(r"+------------------------------------------------+")

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


def question5():
    global points
    print('The Final Question Is \nWhat specific injury did Kamogawa sustain in his final boxing match that forced him to retire?')
    print(r"+----------------------------+")
    print(r"| a - Detached retina        |")
    print(r"| b - Broken right hand      |")
    print(r"| c - Shattered ribs         |")
    print(r"+----------------------------+")

    while True: 
        answer = input('Enter Your Answer a, b or c: ').lower()
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


def all_points():
    print(f'You got {points} out of 5 for the Hard Hajime No Ippo Quiz!')