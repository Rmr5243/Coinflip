import random
count = 0

h = 0
t = 0
flips = 0
n=int(input("Number of coin flips"))
def biasedflip():
   global h
   global t
   if random.randint(1,100) < 65:
      return "tails"
   else:
      return "heads"
   
def FairCoin():
    c1 = biasedflip()
    c2 = biasedflip()
    if c1 == c2:
        return FairCoin()
    else:
        return c1
    
if __name__ == "__main__":
    print ([FairCoin() for _ in range(n)])