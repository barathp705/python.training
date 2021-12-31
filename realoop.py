# real time example of loop
'''
employees=20

#while employees>0:
for employees in range(20,0,-1):
    tim=float(input("Tell us login time: "))
    if tim>=9.16:
        print("You are late to work by",(tim-9.15))
    else:
        print("Have a nice working day")
    #employees-=1
else:
    print("Login Check Done")

    '''
'''
# no of people gonna interviewed 

for count in range(10,0,-1):
    skill=input("Tell us which language u knew: ")
    if skill == 'java' or skill == 'python' or skill=='r':
        print("welcome on the board")
    else:
        print("update yur skill we'll reach you soon")
else:
    print("Interview done")'''

'''
count=10
while count>0:
    skill=input("Tell us which language u knew: ")
    if skill == 'java' or skill == 'python' or skill=='r':
        print("welcome on the board")
        count-=1
    else:
        print("update yur skill we'll reach you soon")
else:
    print("Interview done")'''


# flash sale
sold=0
ordered=0
time=12.01
while time<=12.60:
    count=int(input("Tell us how many mobile you want: "))
    payable=count*14999
    amt=int(input("Enter the amount: "))
    if amt>=payable:
        print("your order of iPhone 13 pro of",count," placed")
        ordered+=1
        sold+=count
    else:
        print("Order couldn't placed because payable is",payable," but available is",amt)
    time+=0.10
else:
    print("Flash sale for iPhone 13 pro is over, total order is",ordered,"and sold mobiles",sold)
