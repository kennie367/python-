#program to calculate bonus earned as per years of service
salary=int(input("Enter the salary: "))
years=int(input("Enter years of service: "))
if years>10:
  bonus=salary*0.1
  print("The bonus is: ",bonus)
if years>=6 and years<=10:
  bonus=salary*0.08
  print("The bonus is: ",bonus)
if years<6:
  bonus=salary*0.05
  print("The bonus is: ",bonus)
    