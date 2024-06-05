l=[3,5,6,"harry"]
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(type(l))

#Negative index

print(l[-3])
print(l[len(l)-3])
print(l[5-3])
print(l[1:-1])
print(l[1:2:3])
print(l[:4])


#list comprehension

l1=[i for i in range(10) if i%2==0]
print(l1)



