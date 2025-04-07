month_number = int(input("Enter the month: "))
month_number1=month_number - 1
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

if 1 <= month_number <= 12:
    print(f"Month {month_number} is {months[month_number1]}")
else:
    print("Invalid")


weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height ** 2)
print(f"Your BMI is:",bmi)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi <= 24.9:
    print("normal")
elif 25 <= bmi <= 29.9:
    print("overweight")
else:
    print("obese")




num = int(input("Enter a number: "))
rev_num = 0

while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num//=10

print("The reversed number is:",rev_num)




while True:
    input_data = input("Enter data:")
    if input_data == "done":
        print("Done")
        break
    print(input_data)

for num in range(1, 10):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j)
      # print()