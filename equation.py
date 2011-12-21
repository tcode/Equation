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

        
        #To figure out where our '=' is in the list
        #This is probably gonna be very unestaestetical.
        #As I think it will rely a good deal on if statements.

        #a=0
        #if list[a]=='=':
        #       workinglist=list[:a] #getting all the part of list up till a
        #
        #Here we are going to do some code to calculate what the parts of the math means
        
        







if __name__=='__main__':
        main()
