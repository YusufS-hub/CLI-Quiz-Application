points = 0


def question1():
    global points
    print('The 1st Question Is \nWhat is the main reason Killua cannot initially command Allukas powers freely?')
    print(r"+---------------------------------------------------------+")
    print(r"| a - He doesn't have enough aura control                 |")
    print(r"| b - Only Nanika chooses who to obey                     |")
    print(r"| c - He must truly consider Alluka a sibling, not a tool |")
    print(r"+---------------------------------------------------------+")

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
      
def question2():
    global points
    print('The 2nd Question Is \nWhat condition does Shoots ability Hotel Rafflesia require to restrain a target?')
    print(r"+----------------------------=================+")
    print(r"| a - They must be injured                    |")
    print(r"| b - He must touch them directly             |")
    print(r"| c - They must enter the confined aura field |")
    print(r"+---------------------------------------------+")

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
    print('The 3rd Question Is \nWhat kind of Nen user is Morel?')
    print(r"+----------------------------+")
    print(r"| a - Transmuter              |")
    print(r"| b - Conjurer                |")
    print(r"| c - Manipulator             |")
    print(r"+----------------------------+")

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
            print('Correct! 1 point')
            points += 1
            break
        elif answer == 'c':
            print('Incorrect!')
            break
    print('\n')


def question4():
    global points
    print('The 4th Question Is \nWhat is the name of the Nen ability Kurapika uses that can only be activated when his eyes are scarlet?')
    print(r"+----------------------------+")
    print(r"| a - Holy Chain             |")
    print(r"| b - Chain Jail             |")
    print(r"| c - Emperor Time           |")
    print(r"+----------------------------+")

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


def question5():
    global points
    print('The Final Question Is \nWhat restriction does Kurapika place on Chain Jail to increase its power?')
    print(r"+-----------------------------------------------------------+")
    print(r"| a - He can only use it during Emperor Time                |")
    print(r"| b - He can only use it on members of the Phantom Troupe   |")
    print(r"| c - He loses a year of his life each use                  |")
    print(r"+-----------------------------------------------------------+")

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
    print(f'You got {points} out of 5 for the Medium HxH Quiz!')