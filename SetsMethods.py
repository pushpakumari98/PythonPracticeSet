#Union and Update

s1={1,2,5,6 }
s2={3,5,8}
print(s1.union(s2))
print(s1,s2)
s1.update(s2)
print(s1,s2)

#Intersection and intersection update

var1={"Mumbai","Kolkata","Jaipur","Hyderabad"}
var2={"chandigarh","Hyderabad","Goa"}
var3=var1.intersection(var2)
print(var3)
var1.intersection_update(var2)
print(var1,var2)

#Symmetric and symmetric difference

v1={2,4,5,7,8}
v2={4,8,9,6}
print(v1.symmetric_difference(v2))

print(v1.difference(v2))
print(v1.difference_update(v2))

#isdisjoint()
a={"good",False,9,3,5}
b={"bad",True,12,8,6}
print(a.isdisjoint(b))

#issuperset()
A={2,3,7,8,9}
B={3,7}
print(A.issuperset(B))

#issubset()
print(B.issubset(A))

#add()
A.add("worst")
print(A)

#update()
cities={"Ayodhya","Varanashi","Banglore"}
cities2={"Haidernagar","Virsa"}
cities.update(cities2)
print(cities)

#remove()/discard()

# cities.remove("moon")
# print(cities)


cities.discard(("moon"))
print(cities)


#pop()
item={2,5,7,9,10}
item2=item.pop()
print(item2)


#del()

# del item2
# print(item2)

#clear()
item.clear()
print(item)


if  'varanashi' in cities:
    print("varanashi is present")

else:
    print("Varanashi is absent")

