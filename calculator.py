#!/usr/bin/env python3
print("\n Welcome to the Calculator v3! \n")

history = []

while True: # Keeps looping until "break"

    action = input("Type one of the following signs: (+) (-) (*) (/) or (H): ")
    
    if action == "H":
        for entry in history:
            print(entry)
        continue

    first = float(input("First Number: "))
    second = float(input("Second Number: "))
    

    if action == "+":
        result = first + second 
        
        
    elif action == "-":
        result =  first - second
        
        
    elif action == "*":
        result = first * second
        
        
    elif action == "/":
        if second == 0.0:
            print("Error! You can't divide by zero! \n\n")
            continue # Returns to the beginning of the loop
        result = first / second
        
        
    else:
        print("Error! Type one of the following signs: (+) (-) (*) (/) \n\n")
        continue

    print(result)
    history.append(f"{first} {action} {second} = {result}")
