#Medium-03

def chk_vow(x,y):
    count=0
    store_V=""
    for i in x:
        if i in y:
            store_V=(store_V+","+i)
            count+=1
    if count==0:
        print("No vowels in the name.")
    else:
        print("Vowels: "+store_V[1:]+". "+"Total number of vowels: "+str(count))

name=input("Enter your name: ")
vow="AaEeIiOoUu"
chk_vow(name,vow)