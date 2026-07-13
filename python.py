#写一个函数求三个数的和，并返回结果
def sum(a,b,c):
    result=a+b+c
    return result

print (sum(3,4,5))


#写一个函数求三个数的平均值，并返回结果
def avg(a,b,c):
    result=sum(a,b,c)/3
    return result

print (avg(3,4,5))


def avg(a,b,c):
    result=(a+b+c)/3
    return result 
print(avg(5,9,17))


#再写一个函数求每个数与平均值之间的差，并返回结果
def diff(a,b,c):
    avg1=avg(a,b,c)
    diff1=a-avg1
    diff2=b-avg1
    diff3=c-avg1
    return diff1,diff2,diff3

print (diff(5,9,17))
