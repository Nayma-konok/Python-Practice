# Write a Python program to print numbers from 1 to 10 using a for loop
for el in range(1,11):
    print(el)

# Write a Python program to calculate the sum of all numbers from 1 to 100 using a for loop.
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

# Write a Python program to display the multiplication table of a given number 
n=int(input("enter a num:"))
for i in range(1,11):
    print(n,"*",i,n*i)

# Write a Python program to reverse a string using a for loop.
text = input("Enter a string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text  # add each character to the front

print("Reversed string:", reversed_text)

# Write a Python program to print all even numbers between 1 and 50 using a for loop.
for i in range(2,50,2):
    print(i)

# Write a Python program to print all odd numbers between 1 and 50 using a for loop.
for i in range(1,50,2):
    print(i)

# Write a Python program to calculate the factorial of a given number using a for loop.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
        factorial *= i  # multiply factorial by i each time
print("The factorial of", num, "is", factorial)

# Write a Python program to count the number of vowels in a given string using a for loop.
# Example: Input: "Hello World" → Output: 3
text = input("Enter a string: ")
vowel="aeiou"
count=0
for char in text:
    if char in vowel:
        count+=1
print(count)

# Write a Python program to generate the first 10 numbers of the Fibonacci sequence using a for loop.
print("the 1st 10 number of Fibonacci sequence")
a = 0
b = 1
for i in range(10):
    print(a)
    c=a+b
    b=a
    a=c

# Write a Python program to print the following pattern using nested for loops:
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):  
    for j in range(i):       
        print("*", end="")    
    print()   