height = input("enter your height in mtrs: ")
weight = input("enter your weight in kgs: ")

print(type(height))
print(type(weight))

bmi = int(weight) / float(height)**2
new_bmi = int(bmi)
print(new_bmi)


