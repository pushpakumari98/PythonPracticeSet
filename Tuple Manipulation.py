"""tuple are immutable so if we want to add,remove,or change tuple items then
first we must convert the tuple to a list """

countries=("spain","Italy","India","England","Germany")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)

countries2=("Australia","Japan","Bangladesh")
new_tuple=countries+countries2
print(new_tuple)

print(countries2.count("Japan"))

tuple1=(0,1,2,3,2,31,1,3,2,3)
res=tuple1.count(3)
print(res)
res=tuple1.index(3)
print(res)
res=tuple1.index(3,4,8)
print(res)