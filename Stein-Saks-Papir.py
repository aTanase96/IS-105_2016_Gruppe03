
"""def main():
    #intro message
    print("Let's play 'Rock, Paper, Scissors'!")
    #call the user's guess function
    number = user_guess()
    #call the computer's number function
    num = computer_number()
    #call the results function
    results(num, number)

#computer_number function
def computer_number():
    #get a random number in the range of 1 through 3
    num = random.randrange(1,4)
    #if/elif statement
    if num == 1:
        print("Computer chooses rock")
    elif num == 2:
        print("Computer chooses paper")
    elif num == 3:
        print("Computer chooses scissors")
    #return the number
    return num

def user_guess():
    # get first guess
    guess = input("Choose 'rock', 'paper', or 'scissors' by typing that word. ")

    # If that guess is invalid, loop until we get a valid guess.
    while not is_valid_guess(guess):
        print('That response is invalid.')
        guess = input("Choose 'rock', 'paper', or 'scissors' by typing that word. ")

    # Now assign the (valid!) guess a number
    # This dictionary is just shorthand for your if/elif chain.
    guess_table = {
        'rock' == 1,
        'paper' == 2,
        'scissors' == 3
    }

    # Return the number associated with the guess.
    return guess[(guess_table)]

def is_valid_guess(guess):
    if is_valid_guess(guess):
        #if/elif statement
        #assign 1 to rock
        if guess == 'rock':
            number = 1
        #assign 2 to paper
        elif guess == 'paper':
            number = 2
        #assign 3 to scissors
        elif guess == 'scissors':
            number = 3
        return number
    else:
        print('That response is invalid.')
        return user_guess() # <-- right her    



#results function
def results(num, number):
    #find the difference in the two numbers
    difference = num - number
    #if/elif statement
    if difference == 0:
        print("TIE!")
        #call restart
        restart()
    elif difference % 3 == 1:
        print("I'm sorry! You lost :(")
        #call restart
        restart()
    elif difference % 3 == 2:
        print("Congratulations! You won :)")
        #call restart
        restart()
        
        def restart():
            answer = input("Would you like to play again? Enter 'y' for yes or \
            'n' for no: ")
            #if/elif statement
            if answer == 'y':
                main()
            elif answer == 'n':
                print("Goodbye!")
            else:
                print("Please enter only 'y' or 'n'!")
                #call restart
                restart()
        

main()"""

#import random module
import random

player = raw_input("Enter your choice (rock/paper/scissors): ")
player = player.lower()
while player != "rock" and player != "paper" and player != "scissors":
    print player
    player = raw_input("That choice is not valid. Enter your choice (rock/paper/scissors): ")
    player = player.lower()
    
    
    
    if player == computer:
        print "Draw!"
    elif player == "rock":
        if computer == "paper":
            print "Computer wins!"
        else:
            print "You win!"
    elif player == "paper":
        if computer == "rock":
            print "You win!"
        else:
            print "Computer wins!"
    elif player == "scissors":
        if computer == "rock":
            print "Computer wins!"
        else:
            print "You win!"    
            
            print "Your choice: " + player + "\nComputer choice: " + computer + "\nThank you for playing!"
            raw_input("Enter any key to exit.")            
            
            