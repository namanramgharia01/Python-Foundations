# PROGRAM TO CALCULATE BILL SPLIT AMONG FRIENDS
total_bill = float(input("Enter the total bill amount: "))
num_friends = int(input("Enter the number of friends: "))
bill_per_person = total_bill / num_friends
print("Each friend should pay: ₹ {:.2f}". format(bill_per_person))
