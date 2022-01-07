'''
functions:
    write once call whenever you want, then it will execute once
    avoid to re write same code for N times

loop:
    executes/repeats the logic until the condition gets failed
    avoid to re write same code for N times

recursive functions:
    change the behaviour of the function work like loop
    call the function from the same function body until some condition gets failed
    eventhough it'll work like loop, it has to be called explicitly once

'''

def eclairs(steps=1):
    print("Android eclairs is old version")
    if steps<=9:
        steps+=1
        eclairs(steps)

#default
eclairs()