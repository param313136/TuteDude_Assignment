
def recursion(num):
    """
    This function is recursive function to calculate the factorial of a number given by user
    :num is number given as input by user
    :return: This function will return 1 if number is less than or equal to 1
    """
    global factorial
    factorial = 1
    if num <= 1:
        return 1
    else:
        factorial= num * recursion(num - 1)
        return factorial

number = int(input("Enter a number : "))
factorial = recursion(number)
print (f"Factorial of {number} is :{factorial}")

