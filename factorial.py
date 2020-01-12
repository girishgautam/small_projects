# for loop

# def fact(num):
#     result = 1
#     for i in range(1, num+1):
#         if i <= 1:
#             result
#         else:
#             result *= i
#     return result


# while loop

# def fact(num):
#     result = 1
#     count = 0
#     while count < num:
#         count += 1
#         result *= count
#     return result


# recursion

# def fact(num):
#     if num <= 1:
#         return num
#     else:
#         return fact(num -1) * num


# Built-in
import math

for i in range(10):
    print('Factorial of ', i , 'is', math.factorial(i))
