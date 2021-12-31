# set: dynamic, no duplicate, no pisition
# list: dynamic, dup, pos : 0
# tuple: static, dup allowed, pos starts from 0

# dictionary{key:value}: dynamic, dup: value, pos is custom key
# eg: contacts,.....

demo={2021:"Covid",4.5:"Zoho","cts":"javascript","places":["chennai","trichy"]}
# printall: list:traverse
# print(demo)
# print all keys alone:
for salem in demo.keys():print(salem)
# print all values alone:
for hey in demo.values():print(hey)
# print pairs one by one:
for k,v in demo.items():print(k,v)


# read
print(demo[2021])
print(demo["places"])
print(demo["places"][0])


# update:
demo[2021]=3000
print("after update in 2021",demo)

# create new
demo[2020]="IT Raise"
'''
# delete:
del demo["places"]
#print(demo["places"])
demo.pop(2021)
#print(demo[2021])
demo.popitem()'''
print(demo)

hai=list(demo.items())

print(hai)

again=dict(hai)

print(again)