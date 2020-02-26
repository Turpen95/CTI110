#CTI - 110
#P3HW2 - BasicMath
#Matthew Turpen
#26 Feb 2020
##Ask the user for input of number1
##Ask the user for input of number2
##Display a menu asking the user which type of math they wish to complete from: Add, Multiply, Subtract or Exit
##Display the result of the math user whishes to be completed from their input.
##Display and error messege if they do not select from the menu.

def main():
    firstNumber = int(input('Enter your first number: '))
    secondNumber = int(input('Enter your second number: '))
    add = firstNumber + secondNumber
    mult = firstNumber * secondNumber
    sub = firstNumber - secondNumber
    print('Please pick from the following choices:')
    print('----------Menu----------')
    choice = input('1) Add Numbers \n2) Multiply Numbers \n3) Subtract Numbers \n4) Exit \n------------------------ \n')

    if choice == '1':
        print(add)
    elif choice == '2':
        print(mult)
    elif choice == '3':
        print(sub)
    elif choice == '4':
        print('The program will now terminate.')
    else:
        print('Please pick a number from the following options only.')
main()
