import math

def main():
       solve()

def solve():
        se = raw_input('Please enter your equation > ')
        a=0
        b=[]
        while a < len(se):
                b.append(se[a])
                a=a+1
                print(b)

        
        a=0
        c=[]
        while a < len(b):
                if b[a]=='=':
                        c=b[:a]
                        
        print(c)
        #To figure out where our '=' is in the list
        #This is probably gonna be very unestaestetical.
        #As I think it will rely a good deal on if statements.

        #All the next code should reside in a loop that goes through the length
        #of the entire list, as to make sure we can find the '='
        #for item in list:
        #       if item=='='
        ##However this seems to be inferior on the level that I still need to know in which
        ##position item is, and that is not so easy with for loops in python, so I might just 
        ##use the while loop as this gives a little better control for this!.
        
        #a=0
        #while a < len(list)
        #if list[a]=='=':
        #       workinglist=list[:a] #getting all the part of list up till a
        #
        #Here we are going to do some code to calculate what the parts of the math means
        #A first thing to do would be to replace ^ with ** so python understand what we really 
        # mean.
        







if __name__=='__main__':
        main()
