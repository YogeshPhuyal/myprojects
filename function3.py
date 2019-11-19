# wap suing  function to find the factorial of a number .

def fact(a):
    fact = a * (a -1)
    return fact

num = int(input("Enter a number\t"))
factorial = fact(num)
print("the factorial pf %s is %s" % (num , factorial))

