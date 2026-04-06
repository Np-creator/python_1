# so let's talk about one of the most important if not the most important  
# tools or aspect of programming language: functions 
# without functions programming would be hell... All of our codes will look like 
# spagetti codes which are extremely hard to wirte and also read 
# the python-syntax of functions looks like this 

def name_of_the_function(): # def follows the function name with (): keep in mind
    return                  # inside the () we also can have parameters 
                            # return means: return the value or the parameters inside 
                            # function, for exm. here we have no values or no special 
                            # order... so the function return nothing.... 

def add(a,b):               # here we have a very simple function and it is adding
    return a+b              # two numbers. in def add (a,b) we have two parameters
print (add(2,4))            # a and b , in the return we have a+b meaning the value 
                            # of the a and b will be added and be returned back at 
                            # printed .... if you run the code you actually see 
                            # 6 in the output 


# we need functions so we avoid typing and repeating the same codes we have 
# inside the projects in order to make the codes more pleasant and easier to 
# run. imagine, we want to code the adding codes every single time inside the 
# compiler.... it would be disastrous and very bad to read. Like  

a = 2 
b = 4 
 
print(a+b)   # now imagine needing that adding for 1200 lines of code 
             # would you rather write the whole damn thing again and 
             # again? or simply writing => def add(a,b) ?  


def math(x):      # example one 
    return x**2   # mathematical phrase
print(math(2)) 


def name(user_name="Alex"):
    return user_name
print(name("Bob")) 

# think about making a def() by yourself...
# EX: 3 cars - print out their models,prices, built year
# Mercedes E-Class 2002 7,600 Euros
# Ford Mustag 2013 21,000 Euros
# Toyota RAV-4 2025 41,000 Euros

def cars(car1,car2,car3):
    car1 = "Mercdes"
    car2 = "Ford Mustang"
    car3 = "Toyota RAV-4"
    models = car1 , car2, car3
    return models
print(cars("a" , "b" , "c"))

# in this code we get the output like this: ('Mercdes', 'Ford Mustang', 'Toyota RAV-4')
# since we wanna see the car models properly, I need to get back
# and kinda debug it. Debugging > coding all the time
# Also in order to add more values to a one parameter, here for example car pirce, 
# Car model, etc. we shall learn Tuples first! In Tuples we have one parameter 
# which has more than one value! car1 = name = "Mercedes" , year = "2010" , price: 12,000 Euros 
# we will learn it also a little bit later

###########################################################################

# now that we have learned some cool functions and wrote them by ourselves 
# we wanna kinda use them inside a program. 

print(f"The number of {cars} is {math(2)}") 

# as you can see the program just give the output like this:  
# The number of <function cars at 0x10dbf1800> is 4 
# why? Because it cannot go and find the specific car 
# that we have called! 
# To avoid something like that we need a List [] of variable to  
# save codes and save also our time 

#def cars(car1,car2,car3):
#    car1 = "Mercdes"
#    car2 = "Ford Mustang"
#    car3 = "Toyota RAV-4"
#    models = car1 , car2, car3
#    return models
#print(cars("a" , "b" , "c")) 

# instead of writing the madness above we need to  
# just put all cars into one List[] 

def car1(index):
    models = ['Mercedes', 'Mustang' , 'Toyota']
    return models[index]
if car1(1) == "Mercedes": 
    print("Hello")                # here we combined function and if statements 
else: 
    print("False")
print(f"Car is {car1(0)}")

def length(words):
    sum1 = len(words)            # here we wrote a function which prints out
    return sum1                  # the lenght of a String

print(length("hellow"))
print(length("you have done it! "))

# debugging and improving your own code is the most important skill of test everyone
# should have 

def add1(e,f): 
    summe = e + f 
    multip = e * f
    ergebnis = summe,multip          #modified and nicer looking def
    return ergebnis
summe,multip = add1(5,10)      
print(f"Summe: {summe} \n Multiplication is: {multip}")

# the code above is actually the better made code of  
# add() function  
# we have saved the addition inside a summe 
# then at the end we have printed out the summe

first_name = input("Enter name: ")
print(f"Hello {first_name}")
print(f"{first_name} you car is {car1(1)} and your salary is {add1(100,23000)} Euros") 

# you always have a function running inside the program  


if len(first_name) > 2: 
    print(f"You car is {car1(0)} and your salary is equal")
else:
    True


type (add1)     # to see what kind of types our function have 
type (cars)     
type (car1)
type (True)

# so we wanna get the personal infos from a user for ex: 
# name, last name, age 

def personal_data(**data):
    first_name1 = data.get("first_name1", "Max")
    last_name1 = data.get("last_name1" , "Mustermann")
    age1 = data.get("age1" , 18)
    print(f"\033[34m{first_name1}\n{last_name1}\n{age1}\033[34m")

personal_data()


type (personal_data)

def name_2(**list):
    ergebnis = list.get ("ergebnis" , "Hello")
    print(f"\033[35m{ergebnis} is LALA\033[35m")

name_2(ergebnis = "Moin")

def teilnahmer(*liste):
    print(f"\033[31m{liste}\033[31m")
teilnahmer('Ali' , "tino" , "Qtantino")

# wir wollen man jetzt ein Program schreiben 
# in dem der Benutzer begrüsst wird 
# wenn keine Namenangabe => "Max"
# wenn wir selber geben  

def begruessen(name3 = "Max"):       # def () Vorlage
    print(f"Hello {name3}")          # die Funktion

begruessen()                             # because we do not have any name
                                         # the saved name will display (Max)

begruessen("Ali")                        # here we gave the name  

begruessen("Aliiiiii")