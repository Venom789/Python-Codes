class Solution:
    def MissingNumber(self,array,n):
        
        totalsum=((n*(n+1))/2)
        arrsum=0
        for i in array:
            arrsum+=i
            
        return int(totalsum-arrsum)    
    
# Here t is used for taking testcase input 
t=int(input())     
for _ in range(0,t):
    n=int(input())              
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
