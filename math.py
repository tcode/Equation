#!/usr/bin/env python

from math import *
import sys
import wxPython



def triangleArea(a, b, c):
        d = sqrt((a+b+c)/2)
        print (d*((d-a)*(d-b)*(d-c)))
       


def circleArea(radius):
        print (radius**2*pi)





def circleCircumference(radius):
        print (radius*2*pi)





def rectangleArea(side, wide):
        print (side*wide)





def rectangleCircumference(side, wide):
        print((side*2) + (wide*2))




def sphereArea(radius):
        area = 4/3*pi*radius**3
        print("Your result :", area)





def sphereCicumference(radius):
        area = 4*pi*radius*2
        print(area)




def Find(pat, text):
        match = re.search(pat, text)
        if match: 
                print (match.group())
        else:
                print ("No Match!")




def cosinus(v):
        print(cos(v))


def sinus(v):
        print(sin(v))


def console():
        arg = raw_input (">> ")
        if arg == "sphere":
                print("Sphere, interesting unfortunately this is not implemented yet")
                console()

        elif arg == "exit":
                sys.exit()
        elif arg == "help":
                print("This is help")
                print("Available commands are few still")
        else:
                print("not implemented, or bad command")
                console()



def main():
        print ("I am main")
        console()
        for arg in sys.argv:
                if arg == "":
                        print("empty")
                elif arg == "spherearea":
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











