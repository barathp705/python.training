# control statements:
# if
'''
# Prime check

# main block
number=int(input("Tell us number to check for prime: "))

if number==2 or number==5 or number==7 or number==3 or number%2!=0 and number%3!=0 and number%5!=0 and number%7!=0:
    print(number,"is prime")
else:
    print(number,"is not prime")


'''
'''
dose=int(input("How many vaccine dose you took: "))

if dose>=2:
    print("You can enter into GOA")
else:
    print("SOrry take all doses and try later")

'''

'''balance=8900

age=int(input("Tell us age: "))

if age>=50:
    print("Senior citizen 6.1 percent")
    balance+=(balance*6.1)/100
else:
    print("interest rate is 6.5")
    balance+=(balance*6.5)/100

print("your current balance:",balance)
'''

'''balance=200

user=input("Tell us what you wish to do: ")

if user == "deposit":
    amt=int(input("Tell us amount to deposit: "))
    balance+=amt
    print(amt,"has deposited in your account")
else:
    print("Thanks for coming")
print("your current balance",balance)
'''

balance=200

user=input("Tell us what you wish to do: ")

if user == "deposit":
    amt=int(input("Tell us amount to deposit: "))
    balance+=amt
    print(amt,"has deposited in your account")
elif user == 'withdraw':
    amt=int(input("Tell us amount to withdraw: "))
    if amt<=balance:
        balance-=amt
        print(amt," debited from your account")
    else:
        print(amt,"is insufficient")
else:
    print("Thanks for coming")
print("your current balance",balance)


