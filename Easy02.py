#Easy-02

def bMi(v,m):
    bmi_num=m/v**2
    return bmi_num
    
    
x=int(input("Enter height: "))
x=x/100
y=int(input("Enter weight: "))
store=float("%.1f"%bMi(x,y))

if store<18.5:
    print("Score is",str(store)+".","You are Underweight")
elif store>18.5 and store<24.9:
    print("Score is",str(store)+".","You are Normal")
elif store>25 and store<30:
        print("Score is",str(store)+".","You are Overweight")
elif store>30:
        print("Score is",str(store)+".","You are Obese")