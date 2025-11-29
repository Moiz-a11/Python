
# squares=[]

# for i in range(6):
#     squares.append(i*2)


# print(squares)
# now by using list comprehensions
# sq=[i*1 for i in range(6)]
# print(sq)

#2] replace negative values with zero
nums=[-2,-4,-5,-67,65,4,56]

nums=[0 if val<0 else val for val in nums]
print(nums)