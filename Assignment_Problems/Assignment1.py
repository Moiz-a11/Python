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

list1 = list(map(int ,input("enter 1st list numbers :  ").split()))
list2 = list (map(int , input("enter 2nd list numbers : ").split()))

merged_list = list1+list2

merged_list.sort()
print("final list",merged_list) #sorted_list
