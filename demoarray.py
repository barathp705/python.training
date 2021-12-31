# array: dynamic, dup, pos: 0, specific type of items
# syntax: array('type',[v1,v2,...])

# import reference by module name
import array
bundle=array.array('i',[])

# create/add new
bundle.append(87)
bundle.append(87)
#bundle.append('hey')
print(bundle)

# import array by alias name
# import modulename as alias
import array as ay
pack=ay.array('f',[])
pack.append(2.3)
pack.append(85)
print(pack)


# import specific component from module without refering modulename or alias while using
# from module import component(s),*
from array import array
contain=array('i',[90,12,45,67,10,33,100,45,120,61,66,35])

contain.insert(1,20111)

print(contain)

print(contain.count(45))
print(contain.index(33))

# list via iterate
for pos in range(len(contain)):print(contain[pos])

# update:
# contain[5]=1200
for each in range(len(contain)):
    if contain[each]>=100:
        contain[each]+=20

print("print via for in")
for every in contain:print(every)

print("Reading and slicing")
print(contain[3])
print(contain[:])
print(contain[::-1])
print(contain[:5])
print(contain[7:])
print(contain[2:6])

# deletion
contain.remove(67)
contain.pop()# pos or last
contain.pop(8)
del contain[0]

print(contain)