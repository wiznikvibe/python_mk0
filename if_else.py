print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm:"))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print(f"pay {bill} dollars")
    elif age <= 18:
        bill = 7
        print(f"pay{bill} dollars")
    else:
     bill = 12
     print(f"pay {bill} dollars")
want_picture = input("Do you want a picture? y or n.")
if want_picture == "y":
         new_bill = bill + 3
         print(f"pay {new_bill} dollars")

else:
    print("Grow taller can try again later")
    