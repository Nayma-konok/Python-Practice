#to find the sum of the digit of a number accepted from user
num=int(input("enter the number: "))
sum=0
while num!=0:
    r=num%10
    sum=sum+r
    num=num//10

print("the sum of",num,"is",sum)

#to find the product of the digit of a number accepted from user
num=int(input("enter the number: "))
product=1
while num>0:
    r=num%10
    product*=r
    num=num//10

print("product", product)

# reverse the number accepted from the user##123
num=int(input("enter the number: "))
reverse=0
while num>0:
    r=num%10 
    reverse=reverse*10+r 
    num=num//10 
print("reverse",reverse)

# to print the fibonacci series till n terms(accept n from the user) 
n=int(input("enter the number: "))
f=0
s=1
i=0
while i<n:
    print(f,end=" ")
    next_term=f+s
    f=s
    s=next_term
    i+=1

# to print factorial number accepted from use.
n=int(input("enter the number: "))
i=1
f=1
while n>=i:
    f*=i
    # f*=n
    i+=1
print("factorial",n,"is",f)

#to chech wether the number is Armstrong or not.(armstrong the number is a number to the sum of the cube of its digit) 
num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3  # Cube of the digit
    num //= 10

if sum == original:
    print(original, "is an Armstrong number.")
else:
    print(original, "is not an Armstrong number.")

#to add first n terms of the following series using loop :1/1!+1/2!+1/3!+.....+1/n!
n = int(input("Enter a number: "))
i=1
sum=1
j=0
while i<=n:
    sum=sum*i
    j+=1/sum
    i+=1
print(j)

#write a program to enter the numbers till the users want and at the end it should diplay the the sum of all the numbers entered.
n = int(input("Enter a number: "))
i=1
sum=0
ch="Y"
while i<=n:
    print(i)
    sum+=i
    i+=1
print("sum of the number:",sum)


#to enter the numbers till the user enter ZEro and at the end it should display the count of positive and negative numbers entered.
sump=0
sumn=0
n=1
while n!=0:
    n = int(input("Enter a number: "))
    if n>0:
        sump+=n
    else:
        sumn+=n 
print("positive num sum",sump)  
print("negative num sum",sumn)


        
