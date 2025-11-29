
# keywords : try , except,else,finally  
try:
    x = int(input("enter X : "))
    ans =10/x

except ZeroDivisionError:
        print("divide by zero is not allowed")
        

else:
    print(f"ans = {ans}")


finally:
     print("end of program")