#touples are immutable sequence of values
#use () for touple

tup =(1,2,3,4,3,2,4,52,3,43,4,)
#print(tup)
#print(tup[:3])

sum=0
for i in tup:
    sum+=i

print(sum)

# touple method 
print(tup.index(3)) # gives index of 3
print(tup.count(4)) # gives totle 4 