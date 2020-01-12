# For loop
# def fib(num):
#     a, b = 0, 1
#     for i in range(num):
#         print('Fibonacci of ', i, 'is', a)
#         a, b = b, a + b
# fib(10)

# Recursion
#
# def fib(num):
#     if num <= 1:
#         return num
#     else:
#         return fib(num -1)+ fib(num -2)
#
#


# while loop

def fib(num):
    a, b = 0, 1
    count = 0
    while count < num:
        print('Fibonacci of ', count, 'is', a)
        a, b = b, a+b
        count += 1
    # return count


fib(10)