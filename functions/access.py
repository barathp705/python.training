form=["Sabari","Balaji","Venkat","Razak","Finale"]

import bharath

print(bharath.linear(form,"Venkat"))

import bharath as b

print(b.linear(form,"Finale"))

from bharath import *

print(linear(form,"Mohamed"))

form.sort()

# Balaji, Finale, Razak, Sabari, Venkat

print(binary(form,"Balaji",0,len(form)-1))
print(binary(form,"Venkat",0,len(form)-1))