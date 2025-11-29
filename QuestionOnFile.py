# Q] in which line python word exist in sample.txt
data = True
line=1
word="python"
with open("sample.txt","r") as f:

    while data: # jab tak data valid hai
        data = f.readline()
        if(word in data):
            print(f"word exist in line {line}")
            break # with keyword ke bahar lejata
        print(data)
        line += 1
