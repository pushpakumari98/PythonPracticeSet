#Python docstring are the string literals thats appear right after the definition of a functions ,methods,class or module.

def square(n):
    '''Takes in a number n,returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
