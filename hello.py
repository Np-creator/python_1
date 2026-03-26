def validate_name(name):
    if len(name) < 2 or len(name) > 12:
        print("Wrong name!")
        return False
    return True

def validate_age(age):
    if float(age) < 18 or float(age) > 120:
        print("Wrong age!")
        return False
    return True

name = input("Enter a name: ")
age = input("Enter an age: ")

if validate_name(name) and validate_age(age):
    print(f"Welcome {name}!" f"You'are {age}!")  