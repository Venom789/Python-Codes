#Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 
#For example factorial of 4 is 4*3*2*1 which is 24.
#find factorial of given number
def factorial(n):
    
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

n=int(input())        
print(factorial(n))     