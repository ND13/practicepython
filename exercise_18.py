import random

def check_num(random_num, guess_num):
    cow_bull = [0,0]
    for i in range(len(random_num)):
        if random_num[i] == guess_num[i]:
            cow_bull[0] +=1
        elif guess_num[i] in random_num:
            cow_bull[1] += 1
    return cow_bull

if __name__ =="__main__":
    playing = True
    number = str(random.randint(1000,9999))
    guesses = 0
    print("Lets play a game!")
    print("Try to guess a random number by entering 4 digits (ex. 1234)")
    print("For each number you guess as correct in the number and in the correct place value, you get 1 cow")
    print("For each number you guess as correct in the number, but not in the correct place value you get 1 bull")
    print("Use the cows and bulls to try and guess the number! Good Luck!")
                 
    while playing:
        
        user_guess = input("enter a 4 digit number: ")
        
        if user_guess == "exit":
            break

        cowbullcount = check_num(number, user_guess)
        guesses +=1

        print("you have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[0]==4:
            playing =False
            print("you win the game after this many guesses:  " + str(guesses) + "! The number was " + str(number))
        else:
            print("keep guessing!")

