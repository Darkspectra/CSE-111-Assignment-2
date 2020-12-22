name=input("Enter your mail: ")
n_mail=input("Enter your new domain: ")
store_M=(name[-9:])
f=name.index("@")
if store_M!=n_mail:
    m=name[0:f]+"@"+n_mail
    print("Changed: "+m)
elif store_M==n_mail:
    print("Unchanged: "+name)