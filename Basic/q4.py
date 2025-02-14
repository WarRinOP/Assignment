# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.

lst=[1,2,3,"4",5+7j,(1,2),{1,3}, 4.5, "9", 10]
for i in lst:
    print(i, "data type: ", type(i))