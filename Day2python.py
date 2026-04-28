print("Welcome to the tip Calculator!")
start_bill = int(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
bill_split = int(input("How many people to split the bill?\n"))

tip_percent = tip / 100
total_tip_amount = start_bill * tip_percent
close_bill = start_bill + total_tip_amount
final_bill = round(close_bill / bill_split, 2)
print(f"Each person will pay:${final_bill}")