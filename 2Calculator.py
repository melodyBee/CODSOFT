while True:
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    sign= input("Enter sign: ")
    
    if sign == "+":
        print(num1 + num2)
    elif sign == "-":
        print(num1 - num2)
    elif sign == "*":
        print(num1 * num2)
    elif sign == "/":
        print(num1 / num2)
    else:
        print("Invalid sign")