points = 0


def question1():
    global points
    print('The 1st Question Is \nWhat type of Nen user is Gon?')
    print(r"+----------------------------+")
    print(r"| a - Emitter                |")
    print(r"| b - Enhancer               |")
    print(r"| c - Transmitter            |")
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
        if answer == 'b':
            points += 1    

print('\n')  
      
def question2():
    global points
    print('The 2nd Question Is \nWhich Phantom Troupe member uses a vacuum cleaner as a weapon?')
    print(r"+----------------------------+")
    print(r"| a - Pakunoda               |")
    print(r"| b - Uvogin                 |")
    print(r"| c - Shizuku                |")
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
            print('Incorrect!')
            break
        elif answer == 'c':
            print('Correct! 1 point')
            points += 1
            break
        if answer == 'c':
            points += 1
    print('\n')
    
def question3():
    global points
    print('The 3rd Question Is \nWhat is the name of the exam stage where participants had to cook for the examiner?')
    print(r"+----------------------------+")
    print(r"| a - Stage 2                |")
    print(r"| b - Stage 3                |")
    print(r"| c - Stage 4                |")
    print(r"+----------------------------+")

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
        if answer == 'a':
            points += 1
    print('\n')


def question4():
    global points
    print('The 4th Question Is \nWhich Nen category does Kurapika use when his eyes turn scarlet?')
    print(r"+----------------------------+")
    print(r"| a - Specialist             |")
    print(r"| b - Conjurer               |")
    print(r"| c - Enhancer               |")
    print(r"+----------------------------+")

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
        if answer == 'a':
            points += 1
    print('\n')


def question5():
    global points
    print('The Final Question Is \nWhat is the name of the video game Gon and Killua enter to find clues about Gons father?')
    print(r"+----------------------------+")
    print(r"| a - Hunters Arena          |")
    print(r"| b - Greed Island           |")
    print(r"| c - Nen World              |")
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


def all_points():
    print(f'You got {points} out of 5 for the Easy HxH Quiz!')