'''
print("hello world")

# a=input("number dalo jee")
# print(a)

sum = 1 + 2 + 3 + 4 + 5 + 6 + \
    7 + 8 + 9 + 10 + 11 + 12 + \
        13 
print(sum)
'''

name = "Asmit Sahu"
print(name)
print(name[0:3] ,"slicing")

print(name[::3])
print(name[1:3:4])

print(len(name))

print(name.upper())
print(name.lower())

print(name.find("As"))

new_name=name.replace("Sahu","Patel")
print(new_name)

for i in range(1,5):
    if(i==2):
        print("2 agaya")
    elif(i==4):
        print("4 agaya")
    else:
        print("hello")
print("hi")

sum=0
i=0
while i<=5:
    sum+=1
    i+=1
print(sum)