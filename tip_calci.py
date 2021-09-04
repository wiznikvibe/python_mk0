print("Welcome to Tip Calculator")
total_bill = input("What is the total bill?\nRs. ")
tip_percent = input("What percent tip would you like to give? 10, 12, 15?\n ")
per_head = input("How many people to split the bill?\n")
total_bill1 = float(total_bill)
(total_bill)
tip_percent1 = int(tip_percent)
per_head1 = int(per_head)
total_tip = total_bill1 * (tip_percent1/100)
total_amount = total_bill1 + total_tip
tip_pperson = total_tip / per_head1
each_person = total_amount / per_head1
each_person1 = round(each_person,3) 

message = f"Each person has to pay: Rs.{each_person1} "
print(message)
