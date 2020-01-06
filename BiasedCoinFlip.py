import random

h = 0
t = 0
flips = 0
n=int(input("Number of coin flips"))
def biasedflip():
   global h
   global t
   if random.randint(1,100) < 75:
      h += 1
   else:
      t += 1
while flips < n:
   biasedflip()
   flips += 1
ph = (h/n)*100
pt = (t/n)*100
print ("Heads:",h,"Percentage of heads:",ph,"\n","Tails",t,"Percentage of tails:",pt)