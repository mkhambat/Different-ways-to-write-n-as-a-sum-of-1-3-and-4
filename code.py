memo=[]  #Create an empty list called memo (This acts like our DP table)

#Append base cases
memo.append(0)   # 0 can be written in zero ways
memo.append(1)   # 1 can be wriiten in one way (1)
memo.append(1)   # 2 can be wriiten in one way(1+1)
memo.append(2)   # 3 can be written in two ways(1+1+1 or 3)
memo.append(4)   # 4 ways (1+1+1+1 or 3+1 or 1+3 or 4)

n=512555   #Value of input

def count(n):

    if(n<0):
        return 0
    for i in range(5,n+1):   
        memo.append(memo[i-1]%100000 + memo[i-3]%100000 + memo[i-4]%100000)   #Accesses and adds the previously computed values to the next cell in the list(Adds only last 5 digits to the list) 
    return(memo[n])   #Returns the answer
    
count(n)
