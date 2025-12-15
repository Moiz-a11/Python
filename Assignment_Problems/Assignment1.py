# #Assignment 1
# #Q.1]

# name = input("enter  name :")
# age = int(input("enter age  :"))

# print(f"Hello {name} you are {age} years old !")

# #Q.2]

# num1 = int(input("enter num1 : "))
# num2 = float(input("enter num2 :"))
# sum = num1+num2
# difference = num1-num2
# product = num1*num2
# quotiont= num1/num2

# print(f"sum = {sum} , diff = {difference} , product = {product} , quotiont = {quotiont}")

# # Q.3]
# num1 = int(input("enter 1st integer :"))
# num2 = int(input("enter 2nd integer :"))
# num3 = float(input("enter 3rd integer : "))
# float_num1 = float(num1)
# float_num2 = float(num2)
# sum = num1+num2+num3
# average = sum/3
# print(f"average = {average}")

# #Q.4]
# num_str = input("enter num as str :")
# int_num= int(num_str)
# float_num=float(num_str)
# str_num=str(num_str)

# print(type(int_num))
# print(type(float_num))
# print(type(str_num))


# #Q.5]
# x= 10 + 3 * 2 ** 2
# print(x)

# #Assignment 2

# #Q 1]

# salary = int(input("enter salary : "))

# if salary<30000:
#     print("5% tax")
# elif salary>30000 and salary<=70000:
#     print("15% tax")

# elif salary>70000:
#       print("25% tax")
# else:
#      print("not specified:")

# #Q 2]
# def print_even_num(a,b):
#     for num in range(a,b):
#         if(num%2==0):
#             print(num)   

# print_even_num(0,10)

# #Q 3]
# count=0
# def digits_of_num(n):
#     global count
#     while n>0:
#         digit=n%10
#         print(digit)
#         n=n//10  #         n=n//10 gives integer value and   n=n/10 gives float lead to break loop
#         count +=1



# digits_of_num(312)
# print("\n")
# print("count = ",count)

# #Q4] returns sum of digits in n
# def sum_of_digits(n):
#     total=0
#     while n>0:
#         digit = n%10
#         total += digit

#         n=n//10
#     return total   
# print(sum_of_digits(555))

# #Q5] divisible by 3 and 5

# for num in range(0,100):
#     if num % 3 == 0 and num%5 == 0:
#         print(num)

# #Q6]

# while True:
#     user_input =input("enter number or type Quit : ")

#     if user_input=="Quit":
#         break

#     num= int(user_input)

#     if num>0:
#         print("num is positive")

#     elif num<0:
#            print("num is negative")
#     else:
#          print("zero")


#Q10]

# secret_num = 90
# while True: # keeps run program
#     guess = int(input("enter your guess : "))

#     if guess > secret_num:
#         print("Too High")

#     elif guess< secret_num:
#         print("Too Low")
#     else:
#         print("correct !")


#Assignment 3

#Q1]

# str = input("enter str hare : ")

# reversed_str = str[::-1] ,# -1 means reverse direction


# if(reversed_str == str):
#     print("str is palindrome")
# else:
#     print("not a palindrome")

#Q2] avg of all numbers from list

# list = [12,20]

# total = sum(list)
# count = len(list)
# avg = total/count
# print(avg)
#Q3] Inputtwolistsofintegersfromtheuser.Mergethemintoonelistandsorttheresult.

# list1 = list(map(int ,input("enter 1st list numbers :  ").split()))
# list2 = list (map(int , input("enter 2nd list numbers : ").split()))

# merged_list = list1+list2

# merged_list.sort()
# print("final list",merged_list) #sorted_list

#Q4] Givenatupleofintegers,create:Q4•Atupleofallevennumbers•Atupleofalloddnumbers

# numbers=(1,2,3,4,5,6,7,8,9,10)

# even_tup = tuple(i for i in numbers if i % 2 == 0) # first i is for what to store
# odd_tup = tuple( i for i in numbers if i % 2 != 0)

# print(even_tup)
# print(odd_tup)
    
# #Q5]
# dict  =({
#     "name":["ayan","moiz", "shadab","faiz","rehan"],
#     "marks":[89,90,67,78,55],

# })
#Q6]Givenalistofwords:Q6words =["apple","banana","kiwi","cherry","mango"]Createadictionarythatmapseachwordtoitslength.Example:{"apple": 5, "banana": 6, "kiwi": 4, ...}

# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# #word_length= len(words) # ans = 5
# word_length= {word:len(words) for word in words}
# print(word_length)

#Q7] Writeaprogramthattakesastringfromtheuserandprintsthenumberofspacesinthestring

# str = input("enter str here : ")
# #count_spaces = str.count('z')
# #count_spaces = str.count(" ")
# print(count_spaces)

# Q8]Writeaprogramtocheckwhethertwolistssharenocommonelements.share no common elements list1 =[1,2,3,4] list2 =[5,6,7,8]# share common elements list1 =[1,2,3] list2 =[3,4][-usesets]
# def no_common_elements(list1,list2):
#     set1=set(list1)
#     set2=set(list2)

#     if set1.isdisjoint(set2): # sets method , returns true or false
#         print("no common elements")

#     else:
#         print("list share commen elements")



# list1 = [1,2,3]
# list2 = [3,5,6]

# no_common_elements(list1,list2)

#Q9]Givenalist,printallelementsthatappearmorethanonceinthelist.Q9[-usesets]
# numbers =[11,2,3,4,5,11,2,7,2,6,6]
# seen = set()
# duplicates=set()

# for i in numbers:
#     if i in seen:
#         duplicates.add(i)
#     else:
#         seen.add(i)  

# print("elements apearing more than once", duplicates)

#Q10] Asktheuserforastringandprint:Q10•Alluniquecharacters•Thecountofuniquecharacters

# str = input("enter str here : ")
# unique_char = set(str)
# print(unique_char)
# print(len(unique_char))
