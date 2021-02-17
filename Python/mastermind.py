# Simple version of the game 'mastermind'
#----------------------------------------
# Version 1.0       Date: 5 April 2020
#----------------------------------------
# Player vs computer
# A random code gets initialized. The player has 10 guesses to crack the code.
# The game tells the player when it has a right digit in the code but on the wrong
# spot as 'd' (from digit). If a player as a correct digit on the correct spot,
# the game returns a 'c'.

# An example:
#   The code is 1234
#   The player guesses 1359
#   The game will return 'cd' on this guess since 1 is correct and there is a 3.
#-------------------------------------------------------------------------------

                                    ### Packages ###

from random import randint


#------------------------------------------------------------------------------
# Explanation of the game to the player:

print("""
You are about to play a simple version of 'Mastermind'.
The computer will create a code of 4 unique digits from 0-9.
So no 2 the same digits will be used in the code.
You have to guess the code within 10 tries.
After every guess the game will give you feedback.
If you have a correct digit but not in the right place, it will return a 'd'.
if you have a correct digit on the correct spot, it will return a 'c'.

An example:
The code is 1234.
Your guess is 2538.
The game will return 'cd' as feedback.

Good luck!
""")
#------------------------------------------------------------------------------
# Initialization of the code to break:
code = []
while len(code)<4:
    dgt = randint(0,9)
    if dgt not in code:
        code.append(dgt)
    else: pass
print("The code has been initialized.")
#------------------------------------------------------------------------------
# Function that prompts the player for its guess and returns the feedback
def guess():

    print("Make your guess:")
    g = input("> ")

    ges = g.strip()
    if len(ges) != 4 or not ges.isdigit():
        print("You didn't make a proper guess?!")
        print("Type in your guess for the 4-digit code.")
        print("For example 1234 .")
        guess()

    else:
        feedback = ""
        for i in range(len(ges)):

            if int(ges[i]) == code[i]:
                feedback+='c'

            elif int(ges[i]) in code:
                feedback +='d'

            else:
                pass

        return feedback
#------------------------------------------------------------------------------
# Looping over max ammount of guesses.
# Prompting everytime the player for its guess.
# When the player makes a correct guess, stop looping.

found = False
number_of_guesses = 0

while not found and number_of_guesses < 10:
    fdbck = guess()
    number_of_guesses+=1
    #print(fdbck)
    print("\nFeedback on your guess: %s\n" % ''.join(sorted(list(fdbck))))

    if fdbck == 'cccc':
        found = True

    else:
        print("You have %d guesses left." % (10 - number_of_guesses))
#------------------------------------------------------------------------------

if found:
    print("\n\t\t\t***CONGRATULATIONS!***\n\n")
    print("You have beaten the game with %d guesses left!" % (10 - number_of_guesses))

else:
    print("\n\t\t\t***FAIL***\n\n")
    print("Oh, bommer. You didn't manage to guess the correct code in time!")
    print("Better luck next time!")

#------------------------------------------------------------------------------
