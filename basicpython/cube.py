# function to find cube
def cube(num):
    return num * num * num
def divisible3(num1):
    if num1%3==0:
        print("the number is divisible by 3:",cube(num))
    else:
        print("Not a divisible by 3")



num = int(input("enter a number"))
print("The cube of",num," is", cube(num))
divisible3(cube(num))


 