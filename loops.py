# # Print the multiplication table of a number n.
n= int(input("enter number:" ))
i=1
while i<=10:
    print(n*i)
    i+=1
    
# # Print the elements of the following list using a loop:
num=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx=0
while idx<len(num):
    print(num[idx])
    idx+=1

# Print Numbers from 1 to 10.Write a program using a while loop to print numbers from 1 to 10.
i=1
while i<=10:
    print(i)
    i+=1

# Sum of First N Natural Numbers.Ask the user to input a number N. Use a while loop to calculate and print the sum of the first N natural numbers
N=int(input("enter number:" ))
sum=0
num=10
while num>=1:
   sum=num+sum
   num-=1
   print(sum)

#print 1st 10 integers and their squares using while loop
i=1
while i<=10:
   print(i,i**2)
   i+=1

# write loop statement to print the following series 10,20,30,.....300
i=10
while i<=300:
    print(i,end=",")
    i+=10

# write loop statement to print the following series 105,98,91,....7
i=105
while i>=7:
    print(i,end=",")
    i-=7

# print sum of 1st 10 even number
num=2
sum=0
while num<=20:
    print(sum)
    sum=sum+num
    num+=2

# print table of number entered from the user
n=int(input("enter number:"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1

# print all even numbers thal falls betwwn two numbers(exclusive both number) entered from the user.
n1=int(input("enter number1:"))
n2=int(input("enter number2:"))
i=n1
while i<=n2:
    if i%2==0:
        print(i)
        i+=2

# write a programme to check whether the number is prime or not.************
num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    i = 2
    is_prime = True

    while i <= num ** 0.5:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

