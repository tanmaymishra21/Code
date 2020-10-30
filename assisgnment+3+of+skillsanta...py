
# coding: utf-8

# In[1]:


SkillSanta_Dict={"name":"Sachin","age":22,"salary":60000,"city":"New Delhi"}
temp=SkillSanta_Dict["city"]
del SkillSanta_Dict["city"]
SkillSanta_Dict["location"]=temp
print(SkillSanta_Dict)


# In[2]:


import collections
originalList =[11,45,8,11,23,45,23,45,89]
print("Original List : ",originalList)
count = collections.Counter(originalList)
print("Frequency of the elements in the List : ",count)


# In[5]:


sampleList=[87,45,41,65,94,41,99,94]
remove_duplicate=set(sampleList)
print("unique items",list(remove_duplicate))
print("The required tupple is",tuple(remove_duplicate))
print("The maximum number is",max(remove_duplicate))
print("The minimum number is",min(remove_duplicate))


# In[6]:


def showEmployee(name, salary=50000):
    print("Employee", name, "salary is:", salary)
name=str(input("Enter a employee name\n"))
salary=int(input("Enter the salary\n"))
showEmployee(name, salary)
showEmployee(name)


# In[7]:


def outerFunction(a,b):
    def innerFunction(a,b):
        return a+b
    return innerFunction(a,b)+5
num1=int(input("Enter 1st number\n"))
num2=int(input("Enter second number\n"))
outerFunction(num1,num2)


# In[8]:


def fibonacii_recursion(n):
    if n <= 1:
        return n
    else:
        return(fibonacii_recursion(n-1) + fibonacii_recursion(n-2))

nterms = int(input("Enter the length"))

if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fibonacii_recursion(i),end=" ")


# In[9]:


name=str(input("Enter a student name\n"))
age=int(input("Enter the student age\n"))
def displayStudent(name, age):
    print(name, age)
displayStudent(name,age)
showStudent = displayStudent
showStudent(name,age)


# In[10]:


def take_input():
    num = input('Enter Number:\n')
    return num
def mobileNumber(num):
    count=0
    for i in range(0,len(num)):
        if num[i].isdigit()==True:
            count+=1

    if count==10:
        print("Your mobile number is : ",num)
    else:
        print("Enter Your right number\n")
        mobileNumber(take_input())    
mobileNumber(take_input())    


# In[11]:


sentence=str(input("Enter a sentence"))
count_lower=0
count_upper=0
c=0
for i in range(len(sentence)):
    if sentence[i].islower()==True:
        count_lower+=1
    elif sentence[i].isupper()==True:
        count_upper+=1
    else:
        c+=1
print("No. of Uppercase characters :",count_upper)
print("No. of Uppercase characters :",count_lower)


# In[12]:


number=int(input("Enter a number\n"))
sum=0
for i in range(1,number):
    if number%i==0:
        sum=sum+i
if sum==number:
    print("The number is a perfect number")
else:
    print("not perfect")

