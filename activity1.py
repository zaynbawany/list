from operator import add
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
result=list(map(add,list1,list2))
print(result)
def square(n):
    return n*n
number=[2,3,4]
result1=(map(square,number))
print (list(result1))
l1=['a','b','c','d','e']
l2=[1,2,3,4,5]
result2=(zip(l1,l2))
print(list(result2))