#To write a file untill i want to
'''f12=open("File1 .txt",'w')
text=input("write to the file.....write quite stop")
while text!='quit':
    f12.writelines(text+'\n')
    text=input()
print("done with writiing now saving")
f12.close()'''


# code to append text

'''f=open('File1.txt','a')
f.writelines("\n omkar poudel ")
f.close()'''

#code to read
with open("File1.txt","r") as f:
    text = f.read()

print(text)
