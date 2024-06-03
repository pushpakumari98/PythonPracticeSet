a=[1,6,7,8,9,3]
b=["pushpa","Neha","Ayushi"]
print(a,b)
print(len(a))
print(a[1:])
print(a[:3])
a.append(12)
print(a)
a.reverse()
print(a)
print(min(b))
print(max(b))
print(min(a))
print(max(a))

from random import shuffle
shuffle(a)
print(a)