#tuple datatype
# it is faster
#data can't be updated

example_using_constructor = tuple([1,2,3])
example_using_braceket = (1,3)

print(example_using_braceket)
print(example_using_constructor)

#given error while updating

#example_using_braceket[0] = 10
#print(example_using_braceket)

#deleting the tupke data
# operation we can perfrom with tuple
print(dir(example_using_constructor))

#slicing in tuple
print(example_using_braceket[1:])

#tuple vs list
import sys
list_example = [1,2,3,4,5]
tuple_example =( 1,3,4)

print(sys.getsizeof(list_example)) # showing the memory space 
print(sys.getsizeof(tuple_example))
#print(dir(sys)) 

#tuple unpack
new_tuple = (1,[2,3],3)
first, second, third = new_tuple
print(first)
second.append(20)
print(second)
print(third)

#set can't be accessed using index
print(new_tuple)

#set wiht true false 0 1
example_set_boolean ={1,2, True , 0 ,False}
print(example_set_boolean)

#add data
add_example = {1,2,3}
add_example.add(2)
print(add_example)

#adding multiple data using update

add_example.update({5,6,1})
print(add_example)

#remove the data
#it will cause error
add_example.remove(10)
print(add_example)

#usind discard
#it will not cause error
add_example.discard(10)
print(add_example)


