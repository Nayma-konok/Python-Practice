# Write a function to find the maximum of three numbers.
def max_nums(a,b,c):
    m=max(a,b,c)
    return(m)

print(max_nums(15,3,30))

# Create a function that takes a string and returns it reversed.
def  text(n):
    reversed=" "
    for char in n:
        reversed=char+reversed
    return(reversed)
print(text("nayma"))

# Write a function to calculate the factorial of a number (using recursion).
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(6))

# Define a function that checks if a number is prime.
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input("enter a number:"))
if is_prime(n):
    print(True,n,"is a prime number")
else:
    print(False,n,"isn't a prime number")

    
n=int(input("enter a number"))


# Write a function to count the number of vowels in a given string.
def count_vowels(text):
    vowels = "aeiouAEIOU"  
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)

# Write a function to find the sum of all elements in a list.Input: A list of numbers.Output: The sum of the numbers.
def sum_of_list(number):
     total=0
     for num in number:
        total+=num
     return total
     
list=[2,3,4,5,6]
result=sum_of_list(list)
print("sum of list:",result)




          

    