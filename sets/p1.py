#sets are immutable

set1={30,40,50}
set2={10,20,30}

#print(set) # set containe unique value

#empty_set={} # not a empty set it creates a empty dictionary
#print(type(empty_set))

# empty_set1 = set()

# print(type(empty_set1))

# methods of set
#set.add(8080)
#set.remove(111)
# clear() >> remove whole values from 
#set.pop() # removes random value from set
#print(set)


print(set1.union(set2))  # prints alll elements of both sets
print(set1.intersection(set2)) # prints common elements of both set