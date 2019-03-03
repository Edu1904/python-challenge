import csv
import os

total_profit=0
#open and read the file
with open('py_bank.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
 #def some variables
    dates = []
    profits = []
    prof=0
    total_profit=0
    header=next(readcsv)
#    header=header.split(',')

    changes=[]
    change=0
#populate profits and dates list
    for row in readcsv:
        profit = row[1]
        date = row[0]

        dates.append(date)
        profits.append(profit)
    
        total_profit =int(total_profit) + int(profit)
        change_profit=int(profit)- change
        changes.append(change_profit)
    
 # seting change to the current value, to calculate profit change of next value
        change=int(profit)

 #   print(dates)
 #   print(profits)
 #   print (total_profit)
 #   print(changes[3])

 #calculate 
changeslenght=len(changes) 
#print(changeslenght)

proflenght=len(profits)
#print(len(profits))

datelenght=len(dates)
#print (datelenght)

avgprofit=(total_profit)/(proflenght)
#print(int(avgprofit))

changestotal=0

for item in changes:

    changestotal = changestotal + int(item)

changestotal = changestotal - 867884

changeavg = (changestotal)/(changeslenght-1)

#print (changestotal)
#print(changeavg)

#calculate max and min change on profit find the date for each max and min value
maximum = max (changes) 
x= changes.index(max(changes))
#print(dates[x])

minimum = min (changes)
y=changes.index(min(changes))
#print(dates[y])
#print(maximum)
#print(minimum)
fecha1=dates[x]
fecha2=dates[y]

#create print for results
print(' ')
print('Financial Analysis')
print('----------------------------')
print('Total Months:' + str(datelenght))
print('Total: $'+str(total_profit))
print('Average Change: $  ' + str(changeavg))
print('Greatest Increase in Profits:  ' + str(fecha1) +' '+'($' + str(maximum) + ')')
print('Greatest Decrease in Profits:  ' + str(fecha2) +' '+'($'+str(minimum)+')')

#save strings variable to make easier to print on the output text file
total_monthstext=('Total Months:' + str(datelenght))
total_profittext=('Total: $'+str(total_profit))
avg_changetext=('Average Change: $  ' + str(changeavg))
greatest_inctext=('Greatest Increase in Profits:  ' + str(fecha1) +' '+'($' + str(maximum) + ')')
greates_dectext=('Greatest Decrease in Profits:  ' + str(fecha2) +' '+'($'+str(minimum)+')')


#output a text file with the results
f1 = open ("Py_bank_result.txt","w")
f1.write(' \n')
f1.write(' \n')
f1.write('Financial Analysis\n')
f1.write(' \n')
f1.write('----------------------------- \n')
f1.write(' \n')
f1.write(total_monthstext)
f1.write(' \n')
f1.write(' \n')
f1.write(total_profittext)
f1.write(' \n')
f1.write(' \n')
f1.write(avg_changetext)
f1.write(' \n')
f1.write(' \n')
f1.write(greatest_inctext)
f1.write(' \n')
f1.write(' \n')
f1.write(greates_dectext)
f1.write(' \n')
f1.write(' \n')
f1.close()