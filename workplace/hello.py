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

