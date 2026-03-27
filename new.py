# we wanna build a name guessing program 
# the first name1 = "Ali" , name2 = "Robert" , name3 = "Sebs" 
# the user has 3 guesses, each guess costs 1 attemp  

name1 = "Ali" 
name2 = "Robert"
name3 = "Sebs"
 
guess_name = input("Enter a name: ")

attemp = 3

while attemp > 0:  
    if guess_name != name1 or name2 or name3: 
      print(f"You entered {guess_name} that's wrong") 
      attemp -= 1 
      break 
    else:  
       print(f"{guess_name} is correct!!!")
