print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
bill_with_tip = bill + bill * (tip/100)
people = int(input("How many people to split the bill? "))

amount_with_split = bill_with_tip / people
total = round(amount_with_split, 2)
print(f'Each person should pay: ${total}')


# broken down
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f'Each person should pay: ${final_amount}')
