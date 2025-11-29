
#read mode is default mode 
#r reading mode
#w text to overrite means previous data is erased and new data is added
#x creates new and open for writing
#a writing , append at end
#b binary mode
#t text mode
#+ open disk file for update(r&w)
# f = open("sample.txt", "r") # gives file object

# data = f.read() # reads all lines
# data = f.readline() # reads single  line
# print(data)

# f.close()   

#1]

# f = open("sample.txt", "w")
# f.write("sk\n ayesha") 
# f.close()

#2]

# f = open("sample.txt", "a") # gives file object
# f.write("\n new text is being appended \n at end  ")
# f.close()

#3]

# f=open("sample2.txt","x")
# f.write("it is new file ")
# f.close()

# using with keyword
with open("sample.txt","r") as f:
    print(f.read())