
#Q.1]

name = input("enter  name :")
age = int(input("enter age  :"))

print(f"Hello {name} you are {age} years old !")

#Q.2]

num1 = int(input("enter num1 : "))
num2 = float(input("enter num2 :"))
sum = num1+num2
difference = num1-num2
product = num1*num2
quotiont= num1/num2

print(f"sum = {sum} , diff = {difference} , product = {product} , quotiont = {quotiont}")

# Q.3]
num1 = int(input("enter 1st integer :"))
num2 = int(input("enter 2nd integer :"))
num3 = float(input("enter 3rd integer : "))
float_num1 = float(num1)
float_num2 = float(num2)
sum = num1+num2+num3
average = sum/3
print(f"average = {average}")

#Q.4]
num_str = input("enter num as str :")
int_num= int(num_str)
float_num=float(num_str)
str_num=str(num_str)

print(type(int_num))
print(type(float_num))
print(type(str_num))


#Q.5]
x= 10 + 3 * 2 ** 2
print(x)
