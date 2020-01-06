import random
n=int(input("Number of coin flips: \n"))
h = 0
t = 0
flips = 0
hh = 0
ht = 0
while (flips < n):
	hf=random.randint(0,2)
	if (hf==0):
		hh+=1
	if (hf==1):
		hh+=1
	if (hf==2):
		ht+=1
	flips+=1
pht= (ht/n)*100
print ("Head Heads:", hh, "Head Tails:", ht, "Percentage of Heads Tails:",pht)
