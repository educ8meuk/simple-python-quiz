#!/usr/bin/env python

import piface.pfio as pfio
import time

pfio.init()
score = 0
led = 0

# Ask user name and store to variable name

name = raw_input("Please type your name: ")

print "Hi %s." % (name)

# Play? Yes or No

play = raw_input("Are you ready to play? (Yes/No) ")

if ((play) == "Yes"):
        print "OK"
        time.sleep(0.5)
        print "Ready ..."
        time.sleep(0.5)
        print "Let's go!"
        time.sleep(0.2)
        print ""
else:
        print "Gutted"
        time.sleep(1)
        print "Bye"
        time.sleep(1)

# Question 1

# Load question set

# Load question set 1

fileHandle = open ( '/home/pi/projects/Quiz/q1.txt', 'r' )
str1 = fileHandle.read()
fileHandle.close()

# Remove white space from the end of the string

q1 = str1.rstrip()

# Answer 1

fileHandle = open ( '/home/pi/projects/Quiz/a1.txt', 'r' )
str1 = fileHandle.read()
fileHandle.close()

# Remove white space from the end of the string

a1 = str1.rstrip()

# Incorrect &  info 1

fileHandle = open ( '/home/pi/projects/Quiz/f1.txt', 'r' )
str1 = fileHandle.read()
fileHandle.close()

# Remove white space from the end of the string

f1 = str1.rstrip()

# End of question set 1

# Load question set 2

fileHandle = open ( '/home/pi/projects/Quiz/q2.txt', 'r' )
str1 = fileHandle.read()
fileHandle.close()

# Remove white space from the end of the string

q2 = str1.rstrip()

# Answer 2

fileHandle = open ( '/home/pi/projects/Quiz/a2.txt', 'r' )
str1 = fileHandle.read()
fileHandle.close()

# Remove white space from the end of the string

a2 = str1.rstrip()

# Incorrect &  info 2

fileHandle = open ( '/home/pi/projects/Quiz/f2.txt', 'r' )
str1 = fileHandle.read()
fileHandle.close()

# Remove white space from the end of the string

f2 = str1.rstrip()

# End of question set 2

# Load question set 3

fileHandle = open ( '/home/pi/projects/Quiz/q3.txt', 'r' )
str1 = fileHandle.read()
fileHandle.close()

# Remove white space from the end of the string

q3 = str1.rstrip()

# Answer 3

fileHandle = open ( '/home/pi/projects/Quiz/a3.txt', 'r' )
str1 = fileHandle.read()
fileHandle.close()

# Remove white space from the end of the string

a3 = str1.rstrip()

# Incorrect &  info 3

fileHandle = open ( '/home/pi/projects/Quiz/f3.txt', 'r' )
str1 = fileHandle.read()
fileHandle.close()

# Remove white space from the end of the string

f3 = str1.rstrip()

# End of question set 3

# Print Question 1 to screen for user to see

print (q1)
print ""

# User inputs answer

ans = raw_input()

if ((ans) == (a1)):
        print "Well done!"
        score = (score) + 1
        led = (score) - 1
        time.sleep(1)
        print "Your score is %i" % (int(score))
        pfio.init()
        pfio.digital_write(led,1)
        time.sleep(1)
        print ""
else:
        print (f1)
        time.sleep(1)
        score = 0
        pfio.init()
        print ""

# Question 2

print (q2)
print ""

ans = raw_input()

if ((ans) == (a2)):
        print "Well done!"
        score = (score) + 1
        led = (score) - 1
        time.sleep(1)
        print "Your score is %i" % (int(score))
        pfio.init()
        pfio.digital_write(led,1)
        time.sleep(1)
        print ""
else:
        print (f2)

        time.sleep(1)
        score = (score) - 1
        if ((score) < 0):
                score = 0
        else:
                score = (score)
        led = (score) - 1
        if ((led) < 1):
                pfio.init()
        else:
                pfio.init()
                pfio.digital_write(led,1)
        print ""

# Question 3

print (q3)
print ""

ans = raw_input()

if ((ans) == (a3)):
        print "Well done!"
        score = (score) + 1
        led = (score) - 1
        time.sleep(1)
        print "Your score is %i" % (int(score))
        pfio.init()
        pfio.digital_write(led,1)
        time.sleep(1)
        print ""
else:
        print (f3)
        time.sleep(1)
        score = (score) - 1
        if ((score) < 0):
                score = 0
        else:
                score = (score)
        led = (score) - 1
        if ((led) < 1):
                pfio.init()
        else:
                pfio.init()
                pfio.digital_write(led,1)
        print ""

print "Well done %s, you have finished the quiz and scored %i!!" % (name,int(score))
time.sleep(2)
pfio.init()
exit()

