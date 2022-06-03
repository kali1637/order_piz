"""
########################### PIZZA ORDER PROGRAM PROJECT ##################################################
Congratullations, you've got a job at Pyton Pizz. Your first job is to build an automatic pizza order project
Based on a user's order, work out their final bill.

Small Pizza cost = $15
medium pizza cost = $20
large pizza cost = 25
all_veggie small = 3
medium_veggie = 4
large veggie = 5
pepperoni small = +$2
pepperoni for medium or laarge pizza : +$3
extra cheese for any size pizza: +1
############ result will be like this ie
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
your final bill is : $28
"""


print("WELCOME TO PYTHON PIZZA DELIVERIES ! ")

a = [1,2,3,4,5,6,7,8]

for i in a:
    b =0
    if a > b ==0:
        b += a
    else:
        print("error")

bill = 0


size = input("What size pizza do you want ?= ")
add_all_veggie = input("Do you want All veggie 'y' or 'n' ")
add_pepperoni = input("Do you like to add Pepperoni? = 'y' or 'n' ")
extra_cheese = input("Do you want extra Cheese ? = ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You type small letter wrong")
############ Vggie added scond condition ###########
if add_all_veggie == "Y":
    bill = bill + 5

else:
    print("No veggie")
################## Peproni adde small and medum and large price third condition
if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    elif size == "M":
        bill += 4
####### extra cheese added condition
if extra_cheese == "Y":
    bill += 2


############ CALCULATE TAX ##############
tax = 0
final_bill = 0
if size == "S" or "M" or "L":
    tax = bill * 7 / 100
    final_bill = bill + tax

print(f"Total Bill = {bill}")
print(f"Total Tax= {tax}")
print(f"Final Bill With Tax = $ {final_bill} ")

payment = float(input("Enter Amount =  $"))
if payment == final_bill:
    print("Pyment Successfully ! Thank you ")
else:
    print("CARD DECLINE ")