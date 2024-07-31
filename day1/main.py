print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")

people = input("How many people to split the bill? ")

float_bill = float(bill)

float_tip = float(tip)

tot_tip = float_bill * (float_tip / 100)

tot_bill = (float_bill + tot_tip)/int(people)

print(f"Each person should pay: ${round(tot_bill, 2)}")