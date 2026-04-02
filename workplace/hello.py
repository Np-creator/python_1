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
print(cars('1','2','3'))


