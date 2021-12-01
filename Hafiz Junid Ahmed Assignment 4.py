#!/usr/bin/env python
# coding: utf-8

# In[8]:



 #Make a calculator using Python with addition , subtraction ,multiplication ,division and power

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("Enter the operator you want to perform");
operator=input("Enter any operator for operation +, -, *, /,**  ")
result=0
if operator=='+':
    result=num1+num2;
elif operator=='-':
    result=num1-num2;
elif operator=='*':
    result=num1*num2;
elif operator=='/':
    result=num1/num2;
elif operator=='**':
    result=num1**num2;
else:
   print("Your input is not supported");
print(num1,operator,num2,": ",result)


# In[56]:


numeric_value = [ 1, 2, 3, 4, 5]

input1=int(input("Enter input do you want to check is exit in list using for loop "))
# print("Checking if input exists in list")

for i in numeric_value:
   if(i == input1):
       print ("Element Exists")
       break
else:
   print("not exist")



# In[71]:


#Q3#Write a Python script to add a key to a dictionary

dictionary={1:10, 2:20, 3:30,'key':'junaid'}
dictionary[4]=40
print(dictionary)


# In[48]:


#Write a Python program to sum all the numeric items in a dictionary

my_dict_sum = {'data1':10,'data2':20,'data3':30}
print("result all numeric sum",sum(my_dict_sum.values()))


# In[49]:


#Q5Write a program to identify duplicate values from list
list1=[1,2,3,4,5,6,7,8,9,1,2,3,4]
result1=[]
for i in list1:
   if i not in result1:
       result1.append(i)
   else:
       print(i)


# In[50]:


#Q6-Write a Python script to check if a given key already exists in a dictionary
dictionary = {
    "Hafiz": "1",
    "Junaid": "2",
    "Ahmed": "3",
    "Ansari": "4",
   
}

key=input("enter iput do you want to chek  given value exist or not")


if key in dictionary:
    print("Key exists in a list") 
else:
    print("Key does not exist")

