#Hard-02

days=int(input("Enter days: "))
years=days//365
m=days%365
months=m//30
day=m%30
print(str(years)+" years"+", "+str(months)+" months"+" and "+str(day)+" days")