# list: dynamic and positions and duplicates>> crudl

hi=[8.9,"Infosys",3.4,12.7,9.2]
see=[8.9,3.4,12.7,9.2,1.2,3.4,7.2,4.5]

# list: traverse
print(hi)

# for in 
# for point in hi:print(point)

for pos in range(len(hi)):
    print(hi[pos])

# update
hi[1]="ZOHO"

print("update by condition")
for pos in range(len(see)):
    if see[pos] >= 8:
        see[pos]-=0.8
    print(see[pos])

# read and slicing
print("Reading operations with slice")
print(hi[3])
print(see[:])
print(hi[::-1])
print(see[4:])
print(hi[:3])
print(see[1:6])

# deletion
print("deletion process")
del hi[2]
hi.remove(12.7)
print(hi)
hi.pop()# it defaultly remove last item
print(hi)
hi.pop(0)
print(hi)


# create
hi.append(True)
see.append(7.4)
print(hi,see)

# add by position
hi.insert(1,"Spring")
see.insert(3,7.4)

print(hi,see)

print(see.count(7.4))

print(hi.index(True))

print(see.index(7.4))