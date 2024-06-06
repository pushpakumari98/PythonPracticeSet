#It's same like lists but it cannot be modified as it is immutable.

tup=(12,"hello world",6,True)
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(len(tup))
print(tup[-1])

if 6 in tup:
    print("yes 6 is present in this tuple")

tup2=tup[1:4]
print(tup2)


