# User inputs:
# input("instructions") >> str
# type casting: destinationType(data)

# fuel calcaulator:

fuel=int(input("Tell us how many liters filled: "))
kms=int(input("Tell us km drove: "))

'''
print(fuel,type(fuel),kms,type(kms))

fuel=int(fuel)
kms=int(kms)

'''

print(fuel,type(fuel),kms,type(kms))

print(fuel/kms,"ml consumed per km")

print(kms/fuel,"kms driven per liter")