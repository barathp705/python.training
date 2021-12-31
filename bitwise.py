# bitwise operator: & | ^ >> <<


'''
1024 512 256 128 64 32 16 8 4 2 1
   0   0   0   0  0  0  1 0 0 1 1 >>  19 >> verify
   0   1   1   1  0  0  0 0 0 0 1 >> 897 >> maxi
   0   1   1   1  0  0  1 0 0 1 0 >> 915 >> verify
   0   0   0   0  0  0  1 0 0 1 1 >>  19 >> maxi
   0   1   1   1  0  0  0 0 0 0 1 >> 897 >> verify


   0   0   0   0  1  0  1 1 0 1 0 >> 90
   0   0   0   1  0  1  1 1 1 1 0 >> 190
   0   0   0   1  1  1  0 0 1 0 0 >> 228

   0   0   0   1  1  1  1 1 0 1 0 >> 250
   0   0   0   0  0  1  1 1 0 0 0 >> 56
   0   0   0   1  1  1  1 1 0 1 0 >> 250



   0   0   0   0  1  0  1 1 0 1 0 >> 90
'''

delta=90
froyo=250

print(delta&froyo)

print(froyo|56)

print(delta^190)

#shift operator

verify=19
maxi=897

#print(verify>>3)

#print(maxi<<2)

print("Verify data",verify,"maxi value",maxi)

verify^=maxi
maxi^=verify
verify^=maxi

print("Verify data",verify,"maxi value",maxi)

'''
print("-----------------------------sender window--------------------------------")
data=int(input("tell us data to transfer: "))
key=int(input("Shifting key: "))

#encryption
sending=data<<key

print(sending,"has sent to receiver")

print("------------------------------receiver window-----------------------------")
print("received data",sending)
dkey=int(input("Enter the decryption key:"))
found=sending>>dkey

print(found,"decrypted in receiver end")

print(data is found)'''