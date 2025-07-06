def question1():
    print('The First Question Is \nWhat type of Nen user is Gon?')
    print(r"+----------------------------+")
    print(r"| a - Emitter                |")
    print(r"| b - Enhancer               |")
    print(r"| c - Transmitter            |")
    print(r"+----------------------------+")

    answer = input('Enter Your Answer a, b or c: ')
    while True:
        if answer != 'a' and answer != 'b' and answer != 'c':
            print('Enter a, b or c ! ')
            continue
        if answer == 'a':
            print('Incorrect!')
            break
        elif answer == 'b':
            print('Correct! 1 point')
            break
        elif answer == 'c':
            print('Incorrect!')
            break
            
    print('\n')  
      
def question2():
    print('The Second Question Is \nWhich Phantom Troupe member uses a vacuum cleaner as a weapon?')
    print(r"+----------------------------+")
    print(r"| a - Pakunoda               |")
    print(r"| b - Uvogin                 |")
    print(r"| c - Shizuku                |")
    print(r"+----------------------------+")

    answer = input('Enter Your Answer a, b or c: ')
    while True:  
        if answer != 'a' and answer != 'b' and answer != 'c':
            print('Enter a, b or c ! ')
            continue
        if answer == 'a':
            print('Incorrect!')
            break
        elif answer == 'b':
            print('Incorrect!')
            break
        elif answer == 'c':
            print('Correct! 1 point')
            break
        else:
            print('Enter a, b or c ! ')
            continue
    print('\n')
    
def question3():
    print('The Third Question Is \nWhat is the name of the exam stage where participants had to cook for the examiner?')
    print(r"+----------------------------+")
    print(r"| a - Stage 2                |")
    print(r"| b - Stage 3                |")
    print(r"| c - Stage 4                |")
    print(r"+----------------------------+")

    answer = input('Enter Your Answer a, b or c: ')
    while True: 
        if answer != 'a' and answer != 'b' and answer != 'c':
            print('Enter a, b or c ! ')
            continue 
        if answer == 'a':
            print('Correct! 1 point')
            break
        elif answer == 'b':
            print('Incorrect!')
            break
        elif answer == 'c':
            print('Incorrect!')
            break
        else:
            print('Enter a, b or c ! ')
            continue
    print('\n')