'''def rev(s):
    if s == '':
        return ''
    return s[-1]+rev(s[:-1])
s = input("Enter a string: ")
print(f"The reverse string is:{rev(s)}")'''

'''def length(n):
    if n == '':
        return 0
    return 1 + length(n[1:])
n = input("Enter a string:")
print(f"The lenght of the string is:{length(n)}")'''

'''def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1)+fibo(n-2)
n = int(input("Enter a num:"))
print(f"The num at {n} is:{fibo(n)}")'''

'''def mul(a,b):
    if b == 0:
        return 0
    return(a+mul(a,b-1))
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
print(f"{a}x{b}:{a*b}")'''

def numWord(n):
    dict={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    numstr = str(n)
    words=[dict[i] for i in numstr]
    return " ".join(words)
n = input("Enter a number: ")
print(f"{n} = {numWord(n)}")

'''def multiples(n):
    result = []
    for i in range(1,n+1):
        x = [i*j for j in range(1,6)]
        result.append(x)
    return result
n = int(input("Enter a num:"))
print(multiples(n))'''

'''def multiples(n):
    return [[i*j for j in range(1,6)]for i in range(1,n+1)]
n = int(input("Enter a num:"))
print(multiples(n))'''

'''def freq(s):
    f ={}
    for i in s:
        if i.isalpha():
            i = i.lower()
            if i in f:
                f[i]+=1
            else:
                f[i]=1
    return f
s = input("Enter a sentence: ")
frequency = freq(s)
print("Letter Frequency:")
for l,c in sorted(frequency.items()):
    print(f"{l}:{c}")'''

'''def duplicate(x):
    return list(set(x))
x = input("Enter list:")
y = x.split()
print("Original list:",x)
print("List without duplicates:",duplicate(y))'''

'''def csum(x):
    l = []
    s = 0
    for i in x:
        s += i
        l.appends(s)
    return l
a =input("Enter list:")
x=[]
for i in a.split():
    x.append(int(i))
res = sum(x)
print("Original list:",x)
print("Cumulative list:",res)'''       
        
    
