'''
perfect square
$$$$$
$$$$$
$$$$$
$$$$$
$$$$$
'''

count=int(input("Tell us max limit: "))
# perfect square
for row in range(1,count+1):
    for data in range(1,count+1):
        print("$",end="")
    print()

'''
$
$$
$$$
$$$$
$$$$$
'''

# left upper floyd
for row in range(1,count+1):
    for data in range(1,row+1):
        print("$",end="")
    print()

'''
$$$$$
$$$$
$$$
$$
$
'''

#left inverse/lower floyd
for row in range(count,0,-1):
    for data in range(1,row+1):
        print("$",end="")
    print()

'''
    $
   $$
  $$$
 $$$$
$$$$$
'''

# right upper floyd
for row in range(1,count+1):
    for space in range(count-1,row-1,-1):
        print(" ",end="")
    for data in range(1,row+1):
        print("$",end="")
    print()

'''
$$$$$
 $$$$
  $$$
   $$
    $
'''
# right lower floyd
for row in range(count,0,-1):
    for space in range(count-1,row-1,-1):
        print(" ",end="")
    for data in range(1,row+1):
        print("$",end="")
    print()

'''
    $
   $ $
  $ $ $
 $ $ $ $
$ $ $ $ $
'''

for row in range(1,count+1):
    for space in range(count-1,row-1,-1):
        print(" ",end="")
    for data in range(1,row+1):
        print("$ ",end="")
    print()

for row in range(count,0,-1):
    for space in range(count-1,row-1,-1):
        print(" ",end="")
    for data in range(1,row+1):
        print("$ ",end="")
    print()

'''
   $
  $$$
 $$$$$
$$$$$$$
'''
limit=1
for row in range(1,count+1):
    for space in range(count-1,row-1,-1):
        print(" ",end="")
    for data in range(1,limit+1):
        print("$",end="")
    print()
    limit+=2

limit=(count*2)-1
for row in range(count,0,-1):
    for space in range(count-1,row-1,-1):
        print(" ",end="")
    for data in range(1,limit+1):
        print("$",end="")
    print()
    limit-=2