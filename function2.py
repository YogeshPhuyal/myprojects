# write a function to test if a number entered by user is armstrong or not.
#e.g. 371= 3^3+7^3+1^3=371.


def arm(n):
    sum=0
    while n > 0:
         num = n % 10
         sum = sum + num ** 3
         d=n//10
         n=d
    return sum


num = int(input("enter the number\t"))
sum1 = arm(num)
if sum1 == num:
    print("it is armstrong number ")
else:
    print("it is not armstrong number")


