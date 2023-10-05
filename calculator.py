#!/usr/bin/env python3
print("\n Welcome to the Calculator v2! \n")

while True: # Keeps looping until "break"
    first = float(input("First Number: "))
    second = float(input("Second Number: "))
    action = input("Type one of the following signs: (+) (-) (*) (/): ")

    if action == "+":
        result = first + second 
        print(+ result)
        break # Exits loop after successful operation
    elif action == "-":
        result =  first - second
        print(result)
        break # Exits loop after successful operation
    elif action == "*":
        result = first * second
        print(result)
        break # Exits loop after successful operation
    elif action == "/":
        if second == 0.0:
            print("Error! You can't divide by zero! \n\n")
            continue # Returns to the beginning of the loop
        result = first / second
        print(result)
        break # Exits loop after successful operation
    else:
        print("Error! Type one of the following signs: (+) (-) (*) (/) \n\n")


