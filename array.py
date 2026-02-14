# fridah deraso
# implementing arrays in python using list

#creating an empty array
names =[]

# we add items using append()
names.append("naserian")
names.append("najma")
names.append("sasha")
names.append("ruweidha")
names.append("shalin")
names.append("Liam")


# we remove items at the end using pop().
# pop() returns the element that it has removed and which can be stored in a variable
lastname= names.pop() # the last element will be abind to the lastname variable

#we acces element using indexing 
#indexes start from 0
first_element=names[0]
last_element=names[-1]

# if you need to change elements of the array from both sides you can use collections.deque

#you can iterate over an array and access each element
for name in names:
    print(name)  


# array is also used in dats storage

counties=["nyeri","nairobi", "marsabit","bungoma"]
print("counties")
# array is also used in dats storage


counties=["nyeri","nairobi", "marsabit","bungoma"]
print("counties")