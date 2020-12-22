#Easy-03

def cal(x,y,z):
    sum=0
    if y>x:
        for i in range(x,y):
            if i%z==0:
                sum=sum+i
        return sum
    elif x>y:
        print("\nPlease input in right order")

min_num=int(input("Enter a minimum number: "))
max_num=int(input("Enter a maximum number: "))
div_num=int(input("Enter a divisor number: "))
print(cal(min_num,max_num,div_num))