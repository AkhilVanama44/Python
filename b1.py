"""The function accepts an integers arr of size 'length' as its arguments you are required to return the sum of
the second largest elements from the even positions and second smallest from the odd position of given 'arr'.

Assumption:
    All array elements are unique

    Treat the 0th position a seven

Note:
    Retuen 0 if array is empty

    Return 0,if array length is 3 or less than 3

Example:-

    Input

    Arr:3 2 1 7 5 4

    Output

    7


l=int(input())
Arr=list(map(int,input().split()))
e=[]
o=[]
for i in range(length):
    if i%2==0:
        e.append(Arr[i])
    else:
        o.append(Arr[i])
    e=sorted(e)
    o=sorted(o)
    print(e[len(e)-2]+o[len(o)-2])

write a function to volidate if the provided two strings are anagrams or not.if the two strings are anagrams
the return yes otherwise return no.







    
