# Tip Calculator

print('Welcome to the Tip Calculator')
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, 15?"))
people_split = int(input("How many people to split the bill? ")) 

tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
bill_1_person = total_bill / people_split
final_amount = round(bill_1_person, 2) 

final_bill = input(f"Each person should pay ${final_amount}")