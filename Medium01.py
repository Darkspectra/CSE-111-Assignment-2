#Medium-01

def come(v,m="mohakhali"):
    if "beef burger" in v:
        if "mohakhali" in y or y=='':
            return 170+40+170*8/100
        elif "mohakhali" not in y:
            return 170+60+170*8/100
    if "naga drums" in v:
        if "mohakhali" in y or y=='':
            return 200+40+200*8/100
        elif "mohakhali" not in y:
            return 200+60+200*8/100
    if "bbq chicken cheese burger" in v:
        if "mohakhali" in y or y=='':
            return 250+40+250*8/100
        elif "mohakhali" not in y:
            return 250+60+250*8/100

x=input("Enter your order: ")
y=input("Your address: ")
x=x.lower()
y=y.lower()
print(come(x,y))