import random
f = 0
num = random.randint(1, 100)
print "I'm thinking of an number between 1 and 100. Guess it!"
while f == 0:
    # Convert to "input" from "raw_input" to work with 3.x
    theGuess = int(raw_input("Your guess: "))
    if theGuess == num:
         print "Great Job!"
         f = 1
    else:
         print "Try Again."
         if theGuess <= num:
             print "plus"
         else:
             print "moins"
         
