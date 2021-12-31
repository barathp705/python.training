
#set
hai={"Bharath",90,3.4,"Anand",45,78,12,3.4,90,56,9.8}
#tuple
yet=("Cognizant",9.7,12,6.3,False,45,12,"Week",12)
#list
see=[8.9,3.4,12.7,9.2,1.2,3.4,7.2,4.5]

#print(hai[2])
print(type(hai),hai)
print(type(yet),yet)
print(type(see),see)

'''newone=list(hai)
print(type(newone),newone)'''

hai=list(hai)
print(type(hai),hai)
print(hai[2])
hai.append("Zealous")
print(hai)

# deletion:
tobedeleted=[]
for pos in range(len(hai)):
    if type(hai[pos]) == str:
        tobedeleted.append(hai[pos])
print(tobedeleted)
for pos in range(len(tobedeleted)):
    if tobedeleted[pos] in hai:hai.remove(tobedeleted[pos])

print(hai)

hai.reverse()

print(hai)

hai.sort()

print(hai)