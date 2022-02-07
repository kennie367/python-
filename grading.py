#grading system
print("Enter score of five subjects")
mark1=int(input("subject1: "))
mark2=int(input("subject2: "))
mark3=int(input("subject3: "))
mark4=int(input("subject4: "))
mark5=int(input("subject5: "))
total=mark1+mark2+mark3+mark4+mark5
print("The total is",total)
average=total/5
print("The average is: ",average)
if average>=70and average>=100:
  print("The grade is A")
elif average>=60and average<=69:
  print("The grade is B")
elif average>=50and average<=59:
  print("The grade is C")
elif average>=40and average<=49:
  print("The grade is D")
else:
  print("You failed")

