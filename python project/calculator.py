def add(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("simple calulator")
print("1. add a value:")
print("2. subtract a value:")
print("3. multiplication a value:")
print("4. division a value:")
print("5. exit the program")
x=int(input("enter a first value:"))
y=int(input("enter a second value:"))
choice=input("enter your choice:(1/2/3/4/5):")
if choice=='1':
    print("Result:",add(x,y))
elif choice=='2':
    print("Result:",subtraction(x,y))
elif choice=='3':
    print("Result:",multiplication(x,y))
elif choice=='4':
    print("Result:",division(x,y))
elif choice=='5':
    print("exit the program")
else:
    print("enter valid digit")
    





