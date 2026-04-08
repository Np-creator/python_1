def greetings(**user):
    first_name = user.get("first_name", "Anonymous")
    last_name = user.get("last_name", 13)
    print(f"\033[31m Hello {first_name} {last_name} Welcome to hell!\033[31m")
greetings(last_name = "313")

def calculator(*num):
    return num
print(calculator(2,34,0))

def addition(a,b):
    sum = a + b 
    return sum  

def input(c):
     c = input = print(int(("Give a number: ")))
     return c 

print(addition(2,6) + input) 