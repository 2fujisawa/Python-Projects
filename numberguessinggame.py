import random #module random 

randomnumbernum = random.randint(0,101) #generating random numbers in range of 0 to 100

print("welcome to the number guessing game! Your objective is to guess the random number")

playernumber = int(input("Enter the number you are guessing: ")) #taking in a input as a string

while playernumber < 0 or playernumber > 100:
        print("Your number is not whithin the range of 0 to 100")
        playernumber = int(input("Reenter your guessing number: "))


while playernumber != randomnumbernum:
    playernumber = int(input("Reenter your guessing number: "))

    if playernumber < randomnumbernum:
                print("Your guessed number is lower than the random number")
                continue #this is go over the loop again

    elif playernumber > randomnumbernum:
                print("Your guessed number is higher than the random number")
                continue#this is go over the loop again

else: 
        print("Correct, you guessed the correct number")



