weight=float(input("Enter your weight in (kg): "))
height=float(input("Enter your height in (m): "))
bmi=weight/(height**2)
if bmi < 18.5:
  print("Underweight")
else if 18.5 <= bmi <= 24.9 :
  print("Normal")
else if 25 <=bmi<= 29.9:
  print("Overweight")
else:
  print("Obese")