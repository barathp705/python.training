# demo of set class type functions
# set is dynamic storage: Create Read Update Delete List

hai={"Bharath",90,3.4,"Anand",45,78,12,3.4,90,56,9.8}

# list: iterate all
print(hai)

for data in hai:
    print(data)

# read
#print(hai[0])

# deletion
hai.remove(3.4)

# update by pos is not possible in set

#create
hai.add("Zealous")

#update/ replace
hai.add(9.8)


print(hai)
