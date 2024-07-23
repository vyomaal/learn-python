example_dictonary = {
    "college name" : "iims"
    "location" : "bdyek"
    "location" : "abc"
}

#acessing the data
print(example_dictonary["location"])
print(example_dictonary)
#using get
print(example_dictonary.get("college name"))
print(example_dictonary)
# usinf pop
print(example_dictonary.pop("location"))
print(example_dictonary)

#adding data
example_dictonary["established"]= 2010
example_dictonary.update(("total_faculty":5))
print(example_dictonary)

#update
example_dictonary["established"] = 2020
print(example_dictonary)

# to delete 
example_dictonary.pop("establishment","no data")













