
def factorial(num):
    import math
    factorial = math.factorial(num)
    print("The factorial of " + str(num) + " is " + str(factorial))
    pass



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def multiples(numbers, n):
    
    new_list = []
    
    x = 1
    
    while x in numbers:
        if n % x == 0:
            new_list.append(str(x))
        x += 1
    
    print(new_list)
 
    
    
    return
# current problem -- can't use numbers as a list, needs integer
