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




        





def main():
        print ("I am main")
        for arg in sys.argv:
                if arg == "":
                        print("empty")
                elif arg == "spherearea":
                        print("Sphere Area, calculation")
                        a = sys.argv[2]
                        r = int(a)
                        sphereArea(r)
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











