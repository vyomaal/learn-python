x = "hello i am dumb"
print(x[:3]) # first three 
print(x[3:]) # everthing expect the first three
print(x[1:3]) # only the 1 and 3 word
print(x[:-3]) #everthing expect the last three 

#string concatenation

a = "hello"
b = "world"
c = a + b
print(c)

#error wala
age = 36
#age= str(age)
#txt ="my name is jhon, i am "+ age # it will leads to error as string and number can't be concatenated
txt = f"my name is abc, i am {age}" # another way
print(txt)

#ecsape character
print("apple\\s")

# listing

mylist =[1,2,3,4,5,6,7,8,9]
print(mylist[4])
print(mylist[1:8])
print(mylist[-1:-4])

#updating list
 
list = ["apple","banana","mango","gauva","grapes","blueberry"]
#list[2]="pineapple"
list[1:3] ="blackcurrent"
list.append("oranges")
print(list)

# difference between concatenation two list and using extend

a =[1,3,4,5]
b =[3,5,6,7]
a.extend(b) # elemts of b is added to elements of a
a =a+b
print(a)
