#!/usr/bin/env python3

first = float(input("First Number: "))
second = float(input("Second Number: "))
action = input("Type one of the following signs: (+) (-) (*) (/) \n\n")

if action == "+":
    result = first + second
    print(result)
elif action == "-":
    result =  first - second
    print(result)
elif action == "*":
    result = first * second
    print(result)
elif action == "/":
    if second != 0.0:
        result = first / second
        print(result)
    else:
        print("Error! You can't divide by zero! \n\n")
else:
    print("Error! Type one of the following signs: (+) (-) (*) (/) \n\n")

