#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

if (float(hours) <= 40) :
    pay = float(hours) * float(rate)

else :
    overtime = (float(hours) - 40) * float(rate) * .5
    pay = float(hours) * float(rate) + overtime

print('Pay:', pay)