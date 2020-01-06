import random
import xlsxwriter 
from xlwt import Workbook
x=str(input("Number of Tests"))
workbook = xlsxwriter.Workbook(x)
worksheet = workbook.add_worksheet()
worksheet.write('A1','Test')
worksheet.write('B1','Heads')
worksheet.write('C1','Tails')

x = int(x)
tests=0
row = 1
col = 0
while (tests < x):
    h=0
    n=3
    t=0
    flips = 0
    while (flips < n):
        flip=random.randint(0,1)
        if (flip==0):
            h+=1
        elif (flip==1):
            t+=1
        flips+=1
    worksheet.write (row, col, tests)
    worksheet.write (row, col+1, h)
    worksheet.write (row, col+2, t)
    row += 1
    tests += 1
workbook.close()