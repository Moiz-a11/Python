
f = open("sample.txt","r") # gives file object
data = f.read() # reads all lines
data = f.readline() # reads single  line
print(type(data))

f.close()