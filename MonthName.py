from selectors import SelectSelector

# print("Enter Month(1-12):")
# Month_Num=int(input())
# if Month_Num==1:
#     print("Month ",Month_Num ,"is January")
# if Month_Num == 2:
#         print("Month ", Month_Num, "is February")
# if Month_Num==3:
#     print("Month ",Month_Num ,"is March")
# if Month_Num==4:
#     print("Month ",Month_Num ,"is April")
# if Month_Num==5:
#     print("Month ",Month_Num ,"is May")
# if Month_Num==6:
#     print("Month ",Month_Num ,"is June")
# if Month_Num==7:
#     print("Month ",Month_Num ,"is July")
# if Month_Num==8:
#     print("Month ",Month_Num ,"is August")
# if Month_Num==9:
#     print("Month ",Month_Num ,"is September")
# if Month_Num==10:
#     print("Month ",Month_Num ,"October")
# if Month_Num==11:
#     print("Month ",Month_Num ,"is November")
# if Month_Num==12:
#     print("Month ",Month_Num ,"is December")
# if 1 < Month_Num >12:
#     print("Enter number between 1-12 ony")

# Define the full price of the ticket
ticket_price = 6.00
age = int(input("Enter your age: "))
if age < 16:
    Final_ticket_price = ticket_price / 2
elif age >= 60:
    Final_ticket_price = ticket_price / 3
else:
    Final_ticket_price = ticket_price

print("Your ticket costs £{ticket_price:",Final_ticket_price)

