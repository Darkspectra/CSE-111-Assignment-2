#Hard-01

'''from datetime import date
def come(x,y,z):    
     if z<5:
         return x+": "+str(int(0.1*y))
     elif z>=5 and z<=10:
         return x+": "+str(int(0.1*y+5000))
     elif z>10:
         return x+": "+str(int(0.15*y+15000))



p=int(input("Number of employees: "))
r=""
count=0
while count<p:
   d=str(date.today())
   p=int(d[0:4])
   e_name=input("Enter your name: ")
   m_Salary=int(input("Your monthly salary: "))
   em_date=input("Enter your joining date: ")
   result_date=p-int(em_date[0:4])
   r=come(e_name,m_Salary,result_date)
r=r+","
count+=1
print(r)'''