# reverese an array using recursive

from array import *

hi = array('i',[56,98,11,45,23,12,65,78,45,33])

def rev(start=0,end=len(hi)-1):
    if start<end:
        hi[start]^=hi[end]
        hi[end]^=hi[start]
        hi[start]^=hi[end]
        rev(start+1,end-1)
    else:
        print("reverese done")

print(hi)
rev()
print(hi)