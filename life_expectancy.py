age = input("What is your age?:\n ")
new_age = int(age)

years_remaining = 90 - new_age

months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

  

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left to make a difference."
print(message)