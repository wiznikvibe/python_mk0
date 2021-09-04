print("Welcome to BMI Calculator")
height = float(input("What is your height in mtrs?\n "))
weight = int(input("What is your weight?"))

bmi = int(weight) / float(height)**2
new_bmi=round(bmi,2)


if bmi<=18.5:
    print(f"Your bmi is {new_bmi}, You are underweight")
elif bmi <=25:
    print(f"Your bmi is {new_bmi}, You are normal weight")
elif bmi < 30:
    print(f"Your bmi is {new_bmi}, You are slightly overweight")
elif bmi <= 35:
    print(f"Your bmi is {new_bmi}, You are obese") 
else: 
     print(f"Your bmi is {new_bmi}, You are clinically obese")