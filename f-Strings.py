#f-Strins used for String formatting


letter="Hey!My name is {1} and i am from {0}"
country="India"
name="pushpa"
print(letter.format(country,name))

print(f"Hey my name is {{name}} and i am from {{country}}")
print(f"We use f-strings like this:-Hey my name is {name} and i am from {country}")
# txt="for only {price:.3f} dollars!"
# print(txt.format(price=28.34784))

price=98.455
txt=f"For only {price:.2f} dollars"
print(txt)
print(type(f"{2*30}"))