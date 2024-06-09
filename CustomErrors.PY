a=int(input("Enter any value between 5 and 9:"))

if (a<5 or  a>9):
   raise ValueError("value  should be between 5 and 9")

l=[9,7,8,5,2]
ind=int(input("Enter the index:"))
if ind<0 or ind>4:
    raise IndexError("Index value should be between 0 and 4")
elif ind>=0 and ind<=4:
    print(l[ind])


