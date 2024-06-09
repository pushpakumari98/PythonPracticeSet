
a=input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
      print(f"{int(a)} X {i}={int(a)*i}")
except Exception as e: #except
    print("Sorry some error occurred")
print("Some imp lines of code")
print("End of program")

try:
    num=int(input("Enter an integer:"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")
finally:
    print("I am always executed")
    
    
#memory errors,value errors,index errors
#Finally is alwys executed irrespective of the outcome of the try and except

def func1():
 try:
     l=[3,5,7,8]
     n=input("Enter an index:")
     print(l[i])
     return 1
    
 except:
     print("some error occurred")
     return 0
 
 finally:
     print("i am always executed")
    #print("i am always executed")
     
x=func1()
print(x)

    
    
    
    


    