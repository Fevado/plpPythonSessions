def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2  
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error! Division by zero is not allowed.")
                return  
        else:
            print("Invalid operator. Please enter one of the following: +, -, *, /")
            return  

        print(f"The result is: {result}")

    except ValueError:
        print("Error! Invalid input. Please enter a number.")

calculator()