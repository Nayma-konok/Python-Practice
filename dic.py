mydict={
    "table ": ['a piece of furniture”,“list of facts & figures'],
    "cat" : 'a small animal'
}
print(mydict)


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={}

x=int(input("enter phy marks:"))
marks.update({"phy": x})

y=int(input("enter chem marks:"))
marks.update({"chem": x})

z=int(input("enter math marks:"))
marks.update({"maths": x})

print(marks)


# Add a new key "major" with the value "Computer Science".
# Update the "age" to 21.
# Retrieve and print the "grades" list.
# Remove the "major" key from the dictionary.
student={
    "name": "Alice",
    "age" : 20,
    "grades" : [85, 90, 78]
}
student["major"]="computer science"
student.update({"age": 21})
print(student)
print (student.get("grades"))
student.pop("major")
print(student)

# Write a function word_count(sentence) that takes a string sentence as input and returns a dictionary where:
# Keys are the unique words in the sentence.
# Values are the number of times each word appears.
# Print the number of employees in the "IT" department.
# Increase the "Marketing" budget by 10%.
# Add a new department "Finance" with 5 employees and a budget of 40000.
company = {
    "HR": {"employees": 10, "budget": 50000},
    "IT": {"employees": 25, "budget": 120000},
    "Marketing": {"employees": 15, "budget": 70000}
}
print(company["IT"])
company.update({"Marketing":{"employees": 15,"budget": 77000}})
print(company)
company["Finance"]= {"employees": 5,"budget":4000}
print(company)


# Merge dict1 and dict2 into a single dictionary. If a key exists in both, the value from dict2 should overwrite the value from dict1.
# Print the resulting dictionary.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)


