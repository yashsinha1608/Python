#function 

def sum_cal(a,b):
    sum=a+b
    return sum
print(sum_cal(9,11))   

#recurssion 
def show(n):
    if(n==0):
        return n
    print(n)
    show(n-1)
show (5)