#Creating a dictionary

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict)

#Accessing values

value = my_dict['key1']
value2 = my_dict['key2']



print(value)
print(value2)

#Modifying values

my_dict['key1'] = 'new_value'

print(my_dict)

#Adding new key-value pairs

my_dict['new_key'] = 'new_value'

print("---")
print(my_dict)

#Removing key-value pairs 

del my_dict['key1']  # Using del
value = my_dict.pop('key2')  # Using pop() method


#Nesting two dictionaries together
student_dict = {
    "Student1" : {"name": "Anthony Kamunya",
                   "age": 25,
                   "Year of study": 4},
    "Student2": {"name": "Joan Kamweru",
                 "age": 22,
                 "Year of study": 3},
}

print(student_dict)

#Access values
value3= student_dict['Student1']['name']
print(value3)