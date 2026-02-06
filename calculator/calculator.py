import math


exitProgram = False

while True:
    while True:
        userInput = input("Enter the first number (or q for exit): ")
        
        if userInput.lower() == 'q':
            exitProgram = True
            break

        try:
            firstNumber = float(userInput)
            break
        except ValueError:
            print("Invalid input, try again.")
    
    if exitProgram:
        break

    while True:
        userInput = input("Enter the operator (+, -, *, /, ^): ")

        if userInput.lower() == 'q':
            exitProgram = True
            break

        if userInput in ['+', '-', '*', '/', '^']:
            symbol = userInput
            break
        else:
            print("Invalid operator, try again.")
    
    if exitProgram:
        break

    while True:
        userInput = input("Enter the second number: ")
        
        if userInput.lower() == 'q':
            exitProgram = True
            break

        try:
            secondNumber = float(userInput)
            break
        except ValueError:
            print("Invalid input, try again.")
    
    if exitProgram:
        break

    if symbol == '+':
        result = firstNumber + secondNumber
    elif symbol == '-':
        result = firstNumber - secondNumber
    elif symbol == '*':
        result = firstNumber * secondNumber
    elif symbol == '/':
        if secondNumber == 0:
            print("ERROR")
        else:
            result = firstNumber / secondNumber
    elif symbol =='^':
        result = pow(firstNumber, secondNumber)
    
    print(result)

print("Thank you for using my calculator.")