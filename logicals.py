# logicals : and or not >> to combine multiple relational operation

weight=float(input("Tell us your weight: "))

print("Are you in the light weight category: ",(weight>50 and weight<=70))

print("Are you in the zonel championship tournament: ",((weight>70 and weight<=100) or (weight>=35 and weight<=50)))