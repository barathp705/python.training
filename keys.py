# break, continue keywords loop manipulators
'''
hai=1
#for hai in range(1,101):
while hai<=100:
    if hai%5==0:
        hai+=1
        continue
        #break
    print(hai)
    hai+=1'''


seats=1
while seats<=20:
    if seats==10 or seats==14 or seats==8 or seats%3==0:
        seats+=1
        continue
    else:
        amt=int(input("enter the amount: "))
        if amt>=250:
            print("you can travel @",seats)
            seats+=1
        else:
            print("insufficient amount")
