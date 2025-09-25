subjects={'python','java','C++','python','javascript','java','python','java','C++','C'}
print(subjects)
print(len(subjects))


# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
number={9,"9.0"}
print(number)


set= {1, 2, 3, 4, 5}
set.add(6)
set.remove(3)
print(set )

A = {1, 2, 3} 
B = {3, 4, 5}
A.union(B)
print(A)
A.intersection(B)
print(A)
print(A-B)
print(B-A)

# Write a program to find the symmetric difference between two sets: X = {1, 2, 3, 4} and Y = {3, 4, 5, 6}.
X ={1, 2, 3, 4}
Y = {3, 4, 5, 6}
sym_diff=X.symmetric_difference(Y)
print(sym_diff)

# Given a list of numbers [1, 2, 2, 3, 4, 4, 5], remove all duplicates using a set.
numbers=[1, 2, 2, 3, 4, 4, 5]
print(type(numbers))
number1=list(set(numbers))
print(number1)


# Find students who are enrolled in both subjects.
# Find students who are only in the math class.
# Find all students enrolled in either subject.
math_students = {"Alice", "Bob", "Charlie"}
science_students= {"Bob", "Diana", "Charlie"}
students=math_students.intersection(science_students)
print(students)
math_students.union(science_students)
print(math_students)
students=math_students.symmetric_difference(science_students)
print(students)

