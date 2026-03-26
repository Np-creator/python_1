guess_name = input("enter a name: ")

name1 = "Alex"
name2 = "brian"
name3 = "Jash"

attempts = 3

while attempts > 0:
    if guess_name not in [name1, name2, name3]:
        print(guess_name)
        attempts -= 1
        print("Take another guess")
    else:
        break

else:
    print("bye")



#This code needs to be debugged tomorrowWWW