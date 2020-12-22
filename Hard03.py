p=input("Enter: ")
l=len(p)
x=""
if "?" in p:
    d=p.index("? ")
    for i in p[0:d]:
        x=x+i
x=p.split(". ") 

c_store=p.count(". ")
y=x[0].capitalize()
for i in range(1,c_store+1):
    y=y+". "+x[i].capitalize()
print(y)