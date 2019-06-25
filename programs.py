There are 5 employees get the max salary
a=list(map(int,input().split()))
count=0
while True:
    b=a.index(max(a))
    for i in range(len(a)):
        if(i!=b):
            a[i]+=1
    count+=1
    if(len(set(a))==1):
        print(count)
        break

BUBBLE SORT:
  a=list(map(int,input().split()))
  for j in range(len(a)):
    for i in range (len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
        print(a)
        
SELECTION SORT:
a=list(map(int,input().split()))
for i in range(len(a)):
    min=i
    for j in range (i+1,len(a)):
        if a[j]<a[min]:
            min=j
    a[i],a[min]=a[min],a[i]
    print(a)
    
INSERTION SORT:
a=list(map(int,input().split()))
for i in range(len(a)):
    j=i
    while j>0:
        if a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
            j-=1
        else:
            break
    print(a)
    
DECIMAL TO BINARY CONVERSION AND COUNT THEIR NO OF 1's IN IT:
n=int(input())
print(bin(n).count('1'))
    
DECIMAL TO BINARY CONVERSION AND COUNT THEIR NO OF 1's IN IT for 2 input:
n=int(input())
m=int(input())
c=n & m
print (bin(c).count('1'))

PALINDROME WITHOUT REVERSE:
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input(""))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
    
PALINDROME FOR A STRING OF INPUT:
str=input()
n=len(str)
sind=eind=0
for i in range(n):
    for j in range(n-1,i,-1):
        ind1=i
        ind2=j
        while ind1<ind2:
            if str[ind1]!=str[ind2]:
                break
            ind1+=1
            ind2-=1
        if ind1>=ind2:
            if j-i>eind-sind:
                sind=i
                eind=j
print(str[sind:eind+1])
INPUT: my madam's mother tongue is malayalam                                                                                                
OUTPUT:malayalam 
 
FREQUENCY SORT:ERROR
from collections import Counter 
ini_list =list(input().split(" ")) 
print ("initial list", str(ini_list)) 
result = sorted(ini_list, key = ini_list.count) 
print("final list", str(result)) 
  OR
    import operator
from collections import OrderedDict 
li=list(map(int,input().split()))
d=OrderedDict()
for i in li:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
for i in sorted_d:
    for j in range(i[1]):
        print(i[0],end=" ")

