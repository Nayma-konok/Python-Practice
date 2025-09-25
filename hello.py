##Given the list numbers = [10, 20, 30, 40, 50], print the third element.
list= [10,20,30,40,50]
print(list)
print(type(list))
print(list[2])

##Slicing: Extract the first three elements from the tuple colors = ('red', 'blue', 'green', 'yellow', 'purple')
list1=['cat', 'dog', 'rabbit', 'elephant']
print(len(list1))

##Use the .append() method to add the number 6 to the list numbers = [1, 2, 3, 4, 5].Modify the list numbers = [1, 2, 3, 4, 5] to replace the third element with 99.
num = [1, 2, 3, 4, 5] 
num[2]=99
print(num)
num.append(6)
print(num)

##: Sort the list scores = [45, 12, 78, 34, 89] in ascending order.
scores = [45, 12, 78, 34, 89] 
scores.sort()
print(scores)

##11.	Nested Lists: Given the nested list matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], print the element at the second row and third column.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])

##Create a list of squares of numbers from 1 to 10 using list comprehension.
squares=[n for n in range(1,11)]
print(squares)

##14.	Membership Test: Check if the number 50 exists in the list numbers = [10, 20, 30, 40, 50].
numbers = [10, 20, 30, 40, 50]
if (50 in numbers):
    print("yes") 
else:
    print("no")


