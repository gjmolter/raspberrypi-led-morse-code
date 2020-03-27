#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Gabriel Justen Molter
#@gjmolter
#11/09/2015

#Use GPIO 24 (18) AS Out and GROUND (6) as Ground

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#If you're not using GPIO 24, chage number here
pin = 18

GPIO.setup(pin, GPIO.OUT)

def letterSpacing():
    GPIO.output(pin, 0)
    time.sleep(0.3)

def dit():
    GPIO.output(pin, 1)
    time.sleep(0.4)
    letterSpacing()

def dah():
    GPIO.output(pin, 1)
    time.sleep(1.2)
    letterSpacing()

def wordSpacing():
    GPIO.output(pin, 1)
    time.sleep(2.1)

def messageEnd():
    dit()
    dah()
    dit()
    dah()
    dit()
    
    
    
string = raw_input("Please, insert here the text you want to Morsefy: ")
string = string.lower()

for char in string:
    print ("Starting transmition of: %s") % (char)
    if char == "1":
        dit()
        dah()
        dah()
        dah()
        dah()
    elif char == "2":
        dit()
        dit()
        dah()
        dah()
        dah()
    elif char == "3":
        dit()
        dit()
        dit()
        dah()
        dah()
    elif char == "4":
        dit()
        dit()
        dit()
        dit()
        dah()
    elif char == "5":
        dit()
        dit()
        dit()
        dit()
        dit()
    elif char == "6":
        dah()
        dit()
        dit()
        dit()
        dit()
    elif char == "7":
        dah()
        dah()
        dit()
        dit()
        dit()
    elif char == "8":
        dah()
        dah()
        dah()
        dit()
        dit()
    elif char == "9":
        dah()
        dah()
        dah()
        dah()
        dit()
    elif char == "0":
        dah()
        dah()
        dah()
        dah()
        dah()
    elif char == " ":
        wordSpacing()
    elif char == "a":
        dit()
        dah()
    elif char == "b":
        dah()
        dit()
        dit()
        dit()
    elif char == "c":
        dah()
        dit()
        dah()
        dit()
    elif char == "d":
        dah()
        dit()
        dit()
    elif char == "e":
        dit()
    elif char == "f":
        dit()
        dit()
        dah()
        dit()
    elif char == "g":
        dah()
        dah()
        dit()
    elif char == "h":
        dit()
        dit()
        dit()
        dit()
    elif char == "i":
        dit()
        dit()
    elif char == "j":
        dit()
        dah()
        dah()
        dah()
    elif char == "k":
        dah()
        dit()
        dah()
    elif char == "l":
        dit()
        dah()
        dit()
        dit()
    elif char == "m":
        dah()
        dah()
    elif char == "n":
        dah()
        dit()
    elif char == "o":
        dah()
        dah()
        dah()
    elif char == "p":
        dit()
        dah()
        dah()
        dit()
    elif char == "q":
        dah()
        dah()
        dit()
        dah()
    elif char == "r":
        dit()
        dah()
        dit()
    elif char == "s":
        dit()
        dit()
        dit()
    elif char == "t":
        dah()
    elif char == "u":
        dit()
        dit()
        dah()
    elif char == "v":
        dit()
        dit()
        dit()
        dah()
    elif char == "w":
        dit()
        dah()
        dah()
    elif char == "x":
        dah()
        dit()
        dit()
        dah()
    elif char == "y":
        dah()
        dit()
        dah()
        dah()
    elif char == "z":
        dah()
        dah()
        dit()
        dit()
    elif char == ".":
        dit()
        dah()
        dit()
        dah()
        dit()
        dah()
        dah()
        dah()
    elif char == ",":
        dah()
        dah()
        dit()
        dit()
        dah()
        dah()
    elif char == "?":
        dit()
        dit()
        dah()
        dah()
        dit()
        dit()
    elif char == "'":
        dit()
        dah()
        dah()
        dah()
        dah()
        dit()
    elif char == "!":
        dah()
        dit()
        dah()
        dit()
        dah()
        dah()
    elif char == "/":
        dah()
        dit()
        dit()
        dah()
        dit()
    elif char == "\\":
        dah()
        dit()
        dit()
        dah()
        dit()
    elif char == "(":
        dah()
        dit()
        dah()
        dah()
        dit()
    elif char == ")":
        dah()
        dit()
        dah()
        dah()
        dit()
        dah()
    elif char == "&":
        dit()
        dah()
        dit()
        dit()
        dit()
    elif char == ":":
        dah()
        dah()
        dah()
        dah()
        dit()
        dit()
        dit()
    elif char == ";":
        dah()
        dit()
        dah()
        dit()
        dah()
        dit()
    elif char == "=":
        dah()
        dit()
        dit()
        dit()
        dah()
    elif char == "-":
        dah()
        dit()
        dit()
        dit()
        dit()
        dah()
    elif char == "_":
        dit()
        dit()
        dah()
        dah()
        dit()
        dah()
    elif char == "\"":
        dit()
        dah()
        dit()
        dit()
        dah()
        dit()
    elif char == "$":
        dit()
        dit()
        dit()
        dah()
        dit()
        dit()
        dah()
    elif char == "@":
        dit()
        dah()
        dah()
        dit()
        dah()
        dit()
    else:
        print ("Could not Morsefy this character '%s'") % (char)
        
print "Finishing transmission"
wordSpacing()
messageEnd()
