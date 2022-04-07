#A simple method is to first calculate factorial of n, 
#then count trailing 0s in the result,So if we count 5s in prime factors then we Trailing zeros.

#first find factorial of given number
from itertools import count


def factorial(n):
 #(Itetrative program for factorial )   
    """if n < 0:
       return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact"""

#-----------------------OR-------------------------#
    #(Recursive program for factorial)
    return 1 if (n==1) else n*(factorial(n-1))  

    

# Now we have to count trailing zeros in result
def trailingZeroes(n):
    temp=factorial(n)
    if(temp<0):
        return -1
    count=0
    while(temp>0):
        temp2=temp%10
        temp=temp/10
        if(temp2==0):
            count+=1
    return count


n=int(input())  
print("Factorial of",n,"=",factorial(n))      
print("Number of Trailing Zero =",trailingZeroes(n))   
