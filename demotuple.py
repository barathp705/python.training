# tuple>> fixed size not dynamic, it has position>> crudl

yet=("Cognizant",9.7,12,6.3,False,45,12,"Week",12)

# list
print(yet)

for data in yet:print(data)

print("Listing elements via for in range")
for pos in range(len(yet)):
    print(yet[pos])


# deletion
#del yet[0]

#update
#yet[1]+=0.5

# read by positions
print("Readings")
print(yet[3])

# slicing: [start:end]
print(yet[:])

print(yet[::-1])

print(yet[3:])

print(yet[:len(yet)-2])

print(yet[0:4])

# create
#yet.append(7.8)

print(yet.index(45))
#print(yet.index(True))

print(yet.count(12))
print(yet.count(6.3))
