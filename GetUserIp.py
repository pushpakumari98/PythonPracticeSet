a=int(input("Enter the value of 1st no:"))
b=int(input("Enter the value of 2nd no:"))
add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b

'''Different ways to print i python'''
#print using format function
print("add:{0},sub:{1},mul:{2},div:{3},mod:{4}".format(add,sub,mul,div,mod))

#print using padding and precision
print("add:%d,sub:%d,mul:%d,div:%3.4f,mod:%d"%(add,sub,mul,div,mod))

#print or create table on the basis of alignment

print('{0:<4}|{1:<4}|{2:<4}|{3:<4}|{4:<4}'.format("add","sub","mul","div","mod"))
print('{0:>4}|{1:>4}|{2:>4}|{3:>4}|{4:>4}'.format(add,sub,mul,div,mod))

c=input()   #accept String data type by default
print(c)

d=float(input("Enter 1st no:"))
e=float(input("Enter 2nd no:"))
print(d+e)
