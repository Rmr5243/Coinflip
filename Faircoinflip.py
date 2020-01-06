import random
n=int(input("Number of coin flips"))
h=0
t=0
flips = 0
while (flips < n):
    flip=random.randint(0,1)
    if (flip==0):
        h+=1
    elif (flip==1):
        t+=1
    flips+=1
ph = (h/n)*100
pt = (t/n)*100
print ("Heads:",h,"Percentage of heads:",ph,"\n","Tails",t,"Percentage of tails:",pt)