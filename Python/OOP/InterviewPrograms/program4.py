# Find missing number in an array (using summation and XOR operation)

# 1,2,4,5,6,7


# Summation method
# sum of n natural numbers (1-7)  n*(n+1)/2  and sum of numbers present in array and take different between them 
# 3 is the difference

# XOR operation
# XOR of 1 to n natural numbers (1-7) 1 XOR 2 XOR 3 XOR 4 etc



def get_missing_summation(a):
    n = a[-1]
    total = n*(n+1)//2
    sum1 = sum(a)
    print(total-sum1) 

a = [1,2,4,5,6,7]
# get_missing_summation(a)


def get_missing_xor(a):
    n=len(a)
    xor_a=a[0]
    for index in range(1,n):
        xor_a=xor_a^a[index]
    x2 = 0
    for index in range(1,n+2):
        x2=x2^index
    print(xor_a^x2)

get_missing_xor(a) 