# 6. Check Leap Year
year = float(input("Enter the year: "))
if(year%4==0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not leap Year")