# nested loop in real time: theatre, bus, .....
'''
for show in range(1,5):
    tickets=20
    while tickets>0:
        user_count=int(input("tell us how many tickets you want: "))
        if user_count<=tickets:
            payable=user_count*210
            amt=int(input("enter the amount to pay: "))
            if amt>=payable:
                print(user_count,"tickets are booked in",show,"th show")
                tickets-=user_count
            else:
                print("insufficient, payable is",payable)
        else:
            print("available is",tickets)
    print(show,"show is over")
else:
    print("day is over")'''


'''
$$ @@
@@ $@
$@ @@
$$ @@
@@ @@
$$ $$
'''

chart=""

for rows in range(1,8):
    for seat in range(1,5):
        fare=int(input("enter the amount: "))
        if fare>=280:
            print(seat,"ticket booked")
            chart+="$"
        else:
            print("insufficient amount")
            chart+="@"
        if seat==2:
            chart+=" "
    chart+="\n"
else:
    print(chart)
