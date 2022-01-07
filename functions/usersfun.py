'''
functions:
perform spacefic logic whenever make a call
reduce time and space complexity

user defined function:

syntax:
def funName(param):
    #function logic

4 types:
1. fun param with return
2. fun param without return
3. fun no param with return
4. fun no param no return

object: int,float,str,list,set,tuple,arrat,dict can be used as both arg and return:

parameter/argument: object passed to the function while calling
    - default argument
    - positional arugument

returntype: After execution function returns to the caller with some object



'''
'''
hai=['evans','ruffulo','pudd','andrew','tobey','chirs']

# range(init,cond,iter)

# default argument: init, iter
for i in range(len(hai)):print(hai[i])

'''

# deinition
def alpha():
    print("My Defined one")
    for i in range(len(hai)):print(hai[i])

# definition for positional arg accepted function
def beta(annual,asset):
    if annual>=5.6 or asset >= 20:
        print("Business Loan can be offered upto 5Lacks")
    if annual >=2.1 and asset>=10:
        print("Home loan of 5 lacks")
    if annual >= 1.8 or asset >= 10:print("Personal loan 3Lacks")


hai=['evans','ruffulo','pudd','andrew','tobey','chirs']

def delta():
    return hai[::-1]

#default argument
def cosmo(desired=str):
    return desired(hai)

# call
alpha()

# as per same sequence/order in function definition
beta(3.5,8)
# position mentioning as per same sequence
beta(annual=8.2,asset=15)
# positional arg custom sequence call
beta(asset=7,annual=9.2)

# fun no param and with return
tmp=delta()
print(tmp)

print(delta())

print(cosmo(),type(cosmo()))
print(cosmo(set),type(cosmo(set)))