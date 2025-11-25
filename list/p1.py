#list are mutable, use [] for list
marks=[100,34,56,87]
#print(marks)
#marks[2]=999
# print(marks[1])
#print(marks)
#slicing
#print(marks[0:2])
#marks.append(100) # add element at end
#marks.insert(2,666) # insert element at index
#print(marks)
#marks.sort() # sort in assending order
#marks.reverse() sort in dessending order
# print(marks)
# for i in marks:
#     print(i)
ind=0
key=34
for i in marks:
    if(i==key):
        print(ind)
        break
    ind+=1
        