def menu():
    import random
    prompt = input('Do you want to chose the numbers? (y or n) ')
    if prompt == 'y':
        num1 = int(input('Choose the minimum number: '))
        num2 = int(input('Choose the maximum number: '))
        choice = random.randint(num1, num2)
    if prompt == 'n':
        num1 = 1
        num2 = 1000
        choice = random.randint(num1, num2)
    return choice