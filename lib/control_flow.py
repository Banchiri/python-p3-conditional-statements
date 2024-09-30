#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin"  and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else: 
        return "It's perfect out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else: 
        print("Invalid operation!")
        return None


dog = "cuddly"

if dog == "hungry":
    owner = "Refilling the food bowl."
elif dog == "thirsty":
    owner = "Refilling the water bowl."
elif dog == "playful":
    owner = "Playing tug-of-war."
elif dog == "cuddly":
    owner = "snuggling."
else:
    owner = "Reading newspaper."
print(owner)
def control_flow(value):
    if value:
        print("yep!")
    else:
        print("nope!")

print(control_flow(0))
age = 1
is_baby = "baby" if age < 2 else "not a baby"
print(is_baby)