def calculator(num1, num2,operator):
    """a basic calculator program """
    try:
        #type conversions
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed"
            return num1 / num2
        else:
            return 'Enter one of the operators(+,-,*,/,%)'
    except ValueError as e:
        return f"valueError: {e}"
    except TypeError as e:
        return f"Type error : {e}"

#collecting user input
num1 = input('Enter The first Number: ')
num2 = input('Enter The second Number: ')
operator = input('Choose The operator: ')

result = calculator(num1,num2,operator)
print(f'{num1} {operator} {num2} =  {result}')