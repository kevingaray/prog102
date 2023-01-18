# Write a short Python script, that takes two numbers values, where one of them is the hours worked 
# by employee and the other is the rate, the equation to calculate the payment is (hours * rate), 
# but if the hours is more than 40 the equation is (hours * rate + (hours - 40) * rate * 0.5). 
# So we need a script to do this automatically.

# hours = int(input("Insert the hours : "))
# rate = int(input("Insert the rate : "))

# file = open('employees.csv')

with open('employees.csv') as f:
    next(f) # skip header line
    for line in f:
        if line != '\n':
            name,hours,rate=line.split(",")
            hours = int(hours)
            rate = float(rate)

            if hours < 40:
                payment = (hours*rate)
            else:
                payment = (hours * rate + (hours - 40) * rate * 0.5)
            
            print(f"{name}: {payment}")
        

