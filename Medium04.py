#Medium-04

def palindromeCheck(x):
    if x==x[::-1]:
        return True
    else:
        return False
        
store1=input("Enter a name: ")
if " " in store1:
    s= store1.index(" ")
    t_name= store1[:s]+store1[s+1:]
    new_name=t_name
    print(palindromeCheck(new_name))
elif "" in store1:
    print(palindromeCheck(store1))