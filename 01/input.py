mass = input("mass (in kgs): ")
height = input("height (m): ")

mass = float(mass)
height = float(height)
bmi = mass / height ** 2

if bmi < 18:
    print("under weight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("over weight")
else:
    print("obses")
