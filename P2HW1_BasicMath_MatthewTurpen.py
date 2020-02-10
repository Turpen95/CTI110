    #BasicMath Calculator
    #February 3, 2020
    #CTI-110 P2HW1 - Basic Math
    #Matthew Turpen
    #
    
def main():
    #INPUT

    # Ask user for 1st number & store input
    num1 = int(input('What is your first number?'))

    # Ask user for 2st number & store input
    num2 = int(input('What is your second number?'))
    
    #PROCESS
    # Add num 1 and num2 and store num
    mathSum = num1 + num2
    # Multiply num 1 and num2 and store num
    results = num1 * num2
    
    #OUTPUT
    #Display num1, num2, sum and result
    print('Users first number: ', num1)
    print('Users second number: ', num2)
    print('Sum of numbers: ', mathSum)
    print('Result of numbers: ', results)

main()
