ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}

ep1.update(ep2)
print(ep1)
ep1.clear()
print(ep1)

empt={}  #Empty dictionary
print(empt)

ep2.pop(222)
print(ep2)

item1={67:567,78:567,89:345}
item1.popitem()
print(item1)

del item1[67]
print(item1)
