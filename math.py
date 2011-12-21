#!/usr/bin/env python

from math import *
import sys

#All Math functions in this program follows in the next section


def triangleArea(a, b, c):
        d = sqrt((a+b+c)/2)
        return (d*((d-a)*(d-b)*(d-c)))
       

def circleArea(radius):
        return (radius**2*pi)


def circleCircumference(radius):
        return (radius*2*pi)


def rectangleArea(side, wide):
        return (side*wide)


def rectangleCircumference(side, wide):
        return((side*2) + (wide*2))


def sphereArea(radius):
        area = 4/3*pi*radius**3
        return(area)


def sphereCircumference(radius):
        area = 4*pi*radius*2
        return(area)


def cosinus(v):
        return(cos(v))


def sinus(v):
        return(sin(v))


def tangent(v):
        return(tan(v))


# That was all the math functions

def console():
        arg = raw_input (">> ")
        if arg == "sphere":
                print("This is available calculations for Sphere")
                f = raw_input("What function do you want to use ?: ")
                if f == 'area':
                        r = raw_input("What is your radius?: ")
                        r = int(r)
                        print(sphereArea(r))
                        console()
                elif f == 'circumference':        
                        r = raw_input("What is your radius?: ")
                        r = int(r)
                        print(sphereCircumference(r))
                        console()
                else:
                        console()
        elif arg == "exit":
                sys.exit()
        elif arg == "help":
                print("This is help")
                print("Available commands are few still")
                console()
        elif arg == "sin":
                v = raw_print("What value do you want to take Sinus of ?: ")
                v = int(v)
                print(sinus(v))
                console()
        elif arg == "cos":
                v = raw_input("What value do you want Cosinus of ?: ")
                v = int(v)
                print(cosinus(v))
                console()
        elif arg == "tan":
                v = raw_input("What value do you want to take Tangent of ?: ")
                v = int(v)
                print(tangent(v))
                console()
        elif arg == "circle":
                f = raw_input("Do you want the area inside the circle or the circumference ?: ")
                if f == 'circumference':
                        r = raw_input("What is your radius ?: ")
                        r = int(r)
                        print (circleCircumference(r))
                elif f == 'area':
                        r = raw_input("What is your radius ?: ")
                        r = int(r)
                        print (circleArea(r))
                console()
        elif arg == 'triangle':
                a = float(raw_input('what is your first value: '))
                b = float(raw_input('what is your second value: '))
                c = float(raw_input('what is your third value: '))
                print(triangleArea(a,b,c))
        else:
                print("not implemented, or bad command")
                console()



'''
A other nice thing to do would be to implement a regex 
to help handling all the input in the console, and making it a nicer program to
use.
perhaps also implementing something to solve equations step-by-step


'''


def Find(pat, text):
        match = re.search(pat, text)
        if match: 
                print (match.group())
        else:
                print ("No Match!")



def main():
        print ("I am main")
        console()
        for arg in sys.argv:
                if arg == "":
                        print("empty")
                        console()
                elif arg == "spherearea" or "sphere area":
                        print("Sphere Area, calculation")
                        a = sys.argv[2]  
                        r = float(a)
                        sphereArea(r)
                elif arg == "cos":
                        print("Cosinus calculation")
                        a = sys.argv[2]
                        v = float(a)
                        cosinus(v)
                elif arg == "sin":
                        a = sys.argv[2]
                        v = float(a)
                        sinus(v)
                elif arg == "tan":
                        a = sys.argv[2]
                        v = float(a)
                        tangent(v)
                elif arg == "spherecircumference":
                        print("Sphere circumference, calculation")



'''
hello I am a comment
In fact I am a long comment
'''

##########################################################################
###       ### ##### ###            #### ###### ###          ###  ###### ##
### ##### #### ### #########  ######### ###### ### ######## ### # ##### ##
### ##### ##### # ##########  ######### ###### ### ######## ### ## #### ##
###       ###### ###########  #########        ### ######## ### ### ### ##
### ############ ###########  ######### ###### ### ######## ### #### ## ##
### ############ ###########  ######### ###### ### ######## ### ##### # ##
### ############ ###########  ######### ###### ###          ### ######  ##
##########################################################################



if __name__ == '__main__':
        main()

