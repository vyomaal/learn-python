#while loop

i = 0
while i<10:
    print(i)
    i = i + 2

print("done")

# for loop
collegename = "iims"
for l in collegename:
   print(l)

#printing the range of value form 1 > 9 
for i in range(1,10):
    print(i)

#loop over array list or set
collegename = ["iims","nist","kmc",1,2]
for index, value in enumerate(collegename):
    print(collegename)


#loop over dictionry 
collegename = ("iims tuple", "nist tuple","kmc tuple",1,2)
for college in collegename:
    print(collegename)     