year=int(input("Enter the year to check:"))
if ((year%4==0) or (year%100!=0) and (year400==0)) :
  print("leap year")
else:
  print("Not a leap year")