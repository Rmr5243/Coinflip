import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
rolls = 0
n=int(input("Number of dice rolls"))
def biasedroll():
   global one
   global two
   global three
   global four
   global five
   global six
   roll = ((random.randint(1,100))/100)
   if (0 < roll < (1/9)):
      one += 1
   elif (1/9 < roll <= (3/9)):
      two += 1
   elif (3/9 < roll <= (4/9)):
      three += 1
   elif (4/9 < roll <= (6/9)):
      four += 1
   elif (6/9 < roll <= (7/9)):
      five += 1
   elif (7/9 < roll <= 1):
      six += 1
while rolls < n:
   biasedroll()
   rolls += 1
   
ep = ((two+four+six)/n)*100
op = ((one+three+five)/n)*100
lessthanf=((one+two+three)/n)*100
print ("Ones:",one,"Twos:",two,"Threes:",three,"Fours:",four,"Fives:",five,"Sixes:",six,"\n","Even %:",ep,"Odd %:",op,"\n","Less than Four:",lessthanf)