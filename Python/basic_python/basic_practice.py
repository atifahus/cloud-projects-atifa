print("Hello Python")

#I am declaring and initialing variable
name= "Atifa"
print("My name is : "+ name)

'''
I am new to python. I am practicing basic python here.
'''

print(10+12)
print(2**3)
print(type(name))

age = 12
age = 30
print (age)

height= 22
width = 10
area = height * width
print(area)

#String
color="white"
#int
x=12
#float
y=1.2
#list
aws=["S3","ES2",12]
#dictionary
menu={
  "dessert": "cake",
  "quantity": 2
}

'''
pop() vs remove()

pop() will delete the data by giving the index position. 
remove() will delete the data by giving the value from the list
'''
aws.pop(1)
print(aws)

aws.remove("S3")
print(aws)


'''
append() vs insert()

append() will add the data at the end of the list
insert() will add the data in the position we declare
'''

aws.append("sns")
print(aws)

aws.insert(0, 123)
print(aws)


