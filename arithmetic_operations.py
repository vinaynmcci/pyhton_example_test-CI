print ("Hello World!!")
print ("hello vinay")

#python progamming for fib series
>>> def fib(n):
>>>     a, b = 0, 1
>>>     while a < n:
>>>         print(a, end=' ')
>>>         a, b = b, a+b
>>>     print()
>>> fib(1000)

#python program to perform < and >
n1 = 2
n2 = 3
#add two numbers n1 and n2
add = n1 + n2
print(add)

# Python Program to Perform Arithmetic Operations

num1 = 10
num2 = 5

# Add Two Numbers
add = num1 + num2

# Subtracting num2 from num1
sub = num1 - num2

# Multiply num1 with num2
multi = num1 * num2

# Divide num1 by num2
div = num1 / num2

# Modulus of num1 and num2
mod = num1 % num2

# Exponent of num1 and num2
expo = num1 ** num2

print("The Sum of {0} and {1} = {2}".format(num1, num2, add))
print("The Subtraction of {0} from {1} = {2}".format(num2, num1, sub))
print("The Multiplication of {0} and {1} = {2}".format(num1, num2, multi))
print("The Division of {0} and {1} = {2}".format(num1, num2, div))
print("The Modulus of {0} and {1} = {2}".format(num1, num2, mod))
print("The Exponent Value of {0} and {1} = {2}".format(num1, num2, expo))
