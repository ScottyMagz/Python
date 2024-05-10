import random 
import numpy as np
from datetime import datetime

#Variables#
dt = datetime.now()
DoW = str 
LhF = int 
DoW = dt.weekday()
Sguess = int
Kguess = int
Tguess = int
odds = float
odds = random.uniform(1.0,4.9)
Ans = int
leader = int
###############################



def calculation(Sguess,Kguess,Tguess,Ans):
    Poll = np.array([Sguess,Kguess,Tguess])
    difference_array = np.absolute(Poll-Ans)
    leader = difference_array.argmin()
    if Sguess == Ans :
        print("Scott Gets it Dead on")
    elif Kguess == Ans :
        print("Keith Gets it Dead on")
    elif Tguess == Ans :
        print("Tyler Gets it Dead on")
    
    if leader == 0:
        print("Scott Wins")
    elif leader == 1:
        print("Keith Wis")
    elif leader == 2:
        print("Tyler Wins")
  


def weekday():
    Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    CrntDay = Days[DoW]
    return CrntDay
    

def main ():
    CrntDay = weekday()
    print(f"Good Morning Happy {CrntDay} ")
    Sguess = int(input("Scott How Many LowHanging Fruit Today? "))
    Kguess = int(input("Keith How Many LowHanging Fruit Today? "))
    Tguess = int(input("Tyler How Many LowHanging Fruit Today? "))
    print(f"Ansers Put in With Scott at {Sguess}, Keith is at {Kguess}, and Tyler sits at {Tguess}. ")
    Ans = int(input("What Was The Real Answer ? "))
    calculation(Sguess,Kguess,Tguess,Ans)
main()