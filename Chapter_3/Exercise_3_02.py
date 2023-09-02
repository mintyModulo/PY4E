# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

hours = input('Enter Hours: ')

try:
    standard_hours = float(hours)
except:
    print('Error, please enter numeric input')
    quit()

rate = input('Enter Rate: ')

try:
    standard_rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

if (standard_hours <= 40):
    pay = standard_hours * standard_rate
else:
    overtime = (standard_hours - 40) * standard_rate * .5
    pay = standard_hours * standard_rate + overtime

print('Pay:', pay)