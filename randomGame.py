#!/usr/bin/python -u

import random

max = 20
number = random.randint(1, max)
tries = 0

while True:
    inputString = "Enter a number between 1 and {}: ".format(max)
    answer = raw_input(inputString)

    if answer.rstrip() == '': continue

    try:
        answer = int(answer.rstrip())
    except:
        print "{} is not a number".format(answer)
        continue

    tries += 1

    if answer == number:
        print "You are correct, it only took you {} tries!".format(tries)
        exit(0)
    elif answer < 1 or answer > max:
        print "I guess you messed up a little."
    elif answer < number:
        print "Sorry, but you guessed too low!"
    elif answer > number:
        print "Sorry, but you guessed too high!"
    else:
        print "Something is wrong, please check your input and this code"
        exit(1)
