#factorial (7)=7*6*5*4*3*2*1=2520
#factorial(6)=6*5*4*3*2*1=720
#factorial(5)=5*4*3*2*1=120
#factorial(4)=4*3*2*1=24
#factorial(0)=1

#factorial(n)=n*factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(6))

#5*factorial(4)
#5*4*factorial(3)
#5*4*3*factorial(2)
#5*4*3*2*factorial(1)


#Write a program to print the fibonacci sequence


def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the nth terms:"))
print("fib of nth terms is:",fibonacci(n))




