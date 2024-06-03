a="Pushpa"
b="Kumari"

#string concatenate
#print(a+" "+b)

#calculate string length
#print(len(a+b))

#print name 5 times
#a=(a+" "+b+" ")*5
#print(a)

#String index and slicing

print(b[3])
print(b[3:])
print(b[:3])
print(b[::3])
print(b[::-1])
print(b[:-1]) #negative slicing
print(b[:-3])

print(b[:6])  #or print(name[0:6]) or print(name[:])
print(b[-3:-1]) #print(b[-3:len(b)-1])
print(b[-1:-3]) #no sense of it from 4:2



a="Universe hai"

#converting to lowercase
print(a.lower())

#converting to uppercase
print(a.upper())

print(a.split())
print(a[1])

#splitting the index based on delimeter

c="ElonMusk,William sakesphere,Mountain"
print(c.split(","))

#strip
var="parul mehta    "
print(var.strip())

#rstrip
var1="!!!haiii!!!"
print(var1.rstrip("!!!"))

#replace
print(var.replace("parul","pushpa"))

#capitalize
var2="parul"
print(var2.capitalize())

#center

print(var2.center(10))

#endswith

print(var1.endswith("!!!"))
print(var.endswith("mehta",5,11))



#Formatting String literals
d="Master Stroke"
print(f"what is this {d}!")

#find
fin="My name is pushpa kumari.My  course of study is BTECH in cse"
print(fin.find("is"))
print(fin.find("specialization"))

#index
print(fin.index("is"))
#print(fin.index("specialization"))

#isalpha

alpha="Currently I have been studying Btech in 2nd yr"
print(alpha.isalpha())


#isalnum
print(alpha.isalnum())


#islower
print(alpha.islower)

#isprintable
variable="We wish you a  merry christmas"
print(variable.isprintable())

#isspace
space="  "
print(space.isspace())
#istitle
doc="My Area Of Interest Is Machine Learning,Deep Learning,Data Analytics"
print(doc.istitle())

#isupper
all="HOW UGLY!"
print(all.isupper())

#replace
print(all.replace("UGLY","BEAUTIFUL!"))

#startswith
print(all.startswith("HOW"))
print(all.startswith("ugly"))

#swapcase
va= "my country name is India"
print(va.swapcase())

#title
Str1="How disgusting!"
print(Str1.title())

#   QUICK QUIZ

nm="harry"
print(nm[-4:-2])




