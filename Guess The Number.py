import simplegui
import random
guesses = 7
secret_number = 0


def new_game():        
    global secret_number
    global guesses
    guesses = int(guesses)
    guesses = 7
    secret_number = random.randrange(0, 100)
    print "WELCOME TO THE GUESSING OF THE NUMBERS GAME!!!"
    
def range100():
    global sercret_number
    secret_number = random.randrange(0, 100)
    print "YOUR RANGE OF GUESSING IS FROM 0 TO 100!!!"
    print "YOU HAVE " + str(guesses) + " GUESSES!!!"
       
def range1000():
    global secret_number
    global guesses
    guesses = 10
    secret_number = random.randrange(0, 1000)    
    print "YOUR RANGE OF GUESSING IS FROM 0 TO 1000!!!"
    print "YOU HAVE " + str(guesses) + " GUESSES!!!"
new_game()    
    
    
    
    
def input_guess(guess):
    global secret_number
    global guesses
    guess = int(guess)
    if guess > secret_number:
        print "Lower"
        guesses = guesses-1
        print "You have " + str(guesses) + " guesses."
    elif guess < secret_number:
        print "Higher"
        guesses = guesses-1
        print "You have " + str(guesses) + " guesses."
    elif guess == secret_number:
        print "You are correct!"
        new_game()
    else:
        print "what"
    if guesses == 0:
        print "YOU LOSE, try again."
        new_game()
        
frame = simplegui.create_frame("Guess the Number", 200, 300)
inp = frame.add_input('What is your guess?', input_guess, 120)
frame.add_button('Range between 0 and 100', range100)
frame.add_button('Range between 0 and 1000', range1000)

frame.start()