#Q) WPP for the sum of odd elements of a square matrix whose ith and jth value is same

'''l1=[[1,3,2],
    [4,5,6],
    [7,8,9]]


i=0
j=0
sum1=0
l=len(l1)
for i in range(0,l):
    for j in range(0,l):
         if(i==j):
            if(l1[i][j]%2!=0):
                sum1=sum1+l1[i][j]
        
print(sum1)'''

#Q) WPP for the product of odd elements of a square matrix whose ith and jth value is same

'''l1=[[1,3,2],
    [4,5,6],
    [7,8,9]]


i=0
j=0
sum1=1
l=len(l1)
for i in range(0,l):
    for j in range(0,l):
         if(i==j):
            if(l1[i][j]%2!=0):
                sum1=sum1*l1[i][j]
        
print(sum1)'''

#Q) wpp to count no.of digits in a number
'''def countDigits(num):
    count=0
    while(num>0):
        
        count=count+1;
        num=num//10
    print(count)
    
num=int(input("Enter the number: "))
countDigits(num)'''

#Q) wpp for sorting
#c logic
'''for(i=0;i<size;i++){
    max=arr[i];
    location=i;
    for(j=1;j<size;j++){
        if(max<arr[i]){
            max=arr[j];
            location=j;
            }
        }
    }'''


'''i=0
for i in range(1,101):
    if(i==10 or i==22 or i==99 or i==97 or i==25 or i==44):
        continue
    print(i,end=" ")'''

'''l=[['rohit',20 ,'rohith@gmail.com','M'],
['mohit','21','mohith@gmail.com','M'],
['vakhil','21','vakhil@gmail.com','M']]'''


                           

'''name=input("Enter name:")

if(name=='rohit'):
    age=20
    email='rohith@gmail.com'
    gender='M'
    print('age=',age)
    print('email=',email)
    print('gender=',gender)
elif(name=='mohit'):
    age=21
    email='mohith@gmail.com '
    gender='M'
    print('age=',age)
    print('email=',email)
    print('gender=',gender)
elif(name=='vakhil'):
    age=21
    email='vakhil@gmail.com '
    gender='M'
    print('age=',age)
    print('email=',email)
    print('gender=',gender)
else:
    print('Invalid input')'''

'''colours  red black yellow pink blue green
 numbers 1 2 3 4
 shapes square circle rectangle'''
 
#black 1 square
'''import random
c=['black','green','blue']
n=[1,2,3]
s=['spade','diamond','flower']
 
c1=random.choice(c)
n1=random.choice(n)
s1=random.choice(s)
 
c2='black'
n2=2
s2='spade'
 
if(c1==c2 and n1==n2 and s1==s2):
     print("You have won lucky draw")
else:
    print("Didn't won")'''
