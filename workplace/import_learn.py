# here it shows how to work with import and libraries 
# in python we have tons of libraries 
# you can also develope your own library 
# here I have created a simple calculator 

# import <Modulname> ===> will give you the access of all 
# the functions inside the library here: add , subs, multi 
# *** imporat <Modulname> as <alias> this one helps a lot
# to write the <Modulname> as something you'd prefer to.  
# from <Modulname> import <Functio_name>  
# for example you just wanna add two number and nothing more 
# you just add the number and finished  


# Notice that the both of the programs shall be saved in one PATH  
# we both have them here in my path 


import calculator

result = calculator.multi (2,10)

print(result) 

import calculator as cr 

result_2 = cr.min (10,2) 
print(result_2)

from calculator import multi 

result_3 = multi(131,19)
print (result_3)

from calculator import daten 
calculator.daten(__name__)

