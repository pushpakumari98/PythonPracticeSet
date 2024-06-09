dic={"Pushpa":"Human being","Spoon":"object"}
print(dic["Pushpa"])

dic1={
    344:"Harry",
    56:"Shubham",
    678:"Zakir",
    567:"Neha"
}

print(dic1[567])
print(dic["Spoon"])
print(dic1.get(678))

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key])

for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")

print(dic.items())

for key,value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")

