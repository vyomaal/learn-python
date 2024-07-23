# conditional 
from datetime import date


a= True
if a:
    print("i have value")
else:
    print("i don't have a value")    

# == check two value are equal 
college_name = "iims"
if college_name == "iims":
    print(college_name)
elif college_name == "trinity":
    print("go to trinity")
else:
    print("stay at home")

#not equal to i.e 
data = 10
if data!= 10:
    print("found")
else:
    print(" not found")

#nested if
admin = True
belong_to = "BHM"
if admin:
    if belong_to == "BIT":
        print("welcome to bit")
    else:
        print("belong to different one")
else:
    print("acess denied")    

#boolean check

def go_to_college():
    return "college"

def study_back():
    return "class 10"

passclass10 = True
if passclass10:
    print(go_to_college())
else:
    print(study_back())


