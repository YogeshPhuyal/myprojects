name=input("enter your name")
while name.isalpha()==False:
    name=input("error")
age=(input("enter your age"))
while age < 19:
        age= (input("enter your correct age "))
mobile=input ("enter your mobile number")
while len(mobile)!= 10 or mobile.isalpha == True:
            mobile=input("enter your correct mobile number")
print("your name is ",name)
print("your age is ",age)
print("your mobile number is ",mobile)

