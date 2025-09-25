##Slicing: Extract the first three elements from the tuple colors = ('red', 'blue', 'green', 'yellow', 'purple').
tup=('red', 'blue', 'green', 'yellow', 'purple')
print(tup)
print(type(tup))
print(tup[:3])

##Unpack the tuple dimensions = (1920, 1080) into two variables, width and height.
dimensions = (1920, 1080)
width,height= dimensions
print(width)
print(height)

##13.	Tuple Conversion: Convert the list names = ['Alice', 'Bob', 'Charlie'] into a tuple.
names = ['Alice', 'Bob', 'Charlie']  
print(type(names))
names_tup=tuple(names)
print(names_tup)
print(type(names_tup))

##Zipping: Combine two lists a = [1, 2, 3] and b = ['x', 'y', 'z'] into a list of tuples using the zip() function
a = [1, 2, 3] 
b = ['x', 'y', 'z'] 
a_tup=tuple(a)
b_tup=tuple(b)
x=zip(a_tup,b_tup)
print(tuple(x))