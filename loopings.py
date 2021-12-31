'''
Looping statements:

to reduce space and time complexity by performing repeatation of specific reusable code

start       initialization
end         condition
step up     iteration

while

for in range

for in >> always points the any storage in order to iterate its all elements

break
continue

'''

'''
# numbers between two user inputs

num1=int(input("Tell us start value:"))#init
num2=int(input("Tell us end value:"))

while num1<=num2:#cond
    print(num1)
    num1+=1 #iter

print("iteration by for in range")

for data in range(num1,num2+1): #range(start,end+1,step up)>> default step up +1
    print(data)'''


hai=[89,12,34,56,78,11,9,45,34,12,78,"Bharath",9.3,False,3.4]

print(hai)

print("Using while to iterate")

pos=0

while pos<len(hai):
    print(hai[pos])
    pos+=1

print("Using for in range to iterate")

for pos in range(5,len(hai)):
    print(hai[pos])

print("using for in to iterate")
for data in hai:
    print(data)