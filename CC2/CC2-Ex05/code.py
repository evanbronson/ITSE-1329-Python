hours = input("Hours: ") #your code goes here
rate = input("Rate: ") #your code goes here
pay = float(hours) * float(rate) 
ot = float(hours)-40 
otr = float(rate)*1.5
otpay = 40*float(rate)+float(ot)*float(otr)

if int(hours) > 40:
    print("Pay:", float(otpay))
else:
    print("Pay:", float(pay))
    