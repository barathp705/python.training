from array import *

hey=array('d',[3.4,9.2,12.5,7.8,4.5,3.3,1.2,7.5])

# linear search: O(n)
def linear(where,data,current=0):
    if type(where) == str or type(where) == list:
        if current<len(where):
            if where[current]==data:
                return current
            else:
                return linear(where,data,current+1)
        else:
            return -1
    else:
        print("invalid storage")

# 9 12 34 56 100        >> 12
# binary search: O(logn)
def binary(where,data,start,end):
    if start<=end:
        mid=(end+start)//2
        if where[mid]==data:return mid
        elif data>where[mid]:return binary(where,data,mid+1,end)
        else:return binary(where,data,start,mid)
    else:return -1


'''print(linear(hey,12.5))
print(linear(hey,3.3))
print(linear(hey,12.1))'''