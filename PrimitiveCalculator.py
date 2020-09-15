import sys

def minimum_calcs(n):
    T=[0 for x in range (n+1)]
    for i in range (2,n+1):
        m1=T[i-1]
        q,r = divmod(i,3)
        m2=T[q] if r==0 else sys.maxsize
        q,r = divmod(i,2)
        m3=T[q] if r==0 else sys.maxsize
        T[i]= 1+ min(m1, m2, m3)
    return T

def get_sequence(n):
    s=[]
    t=minimum_calcs(n)
    i=n
    while i>0:
        s.append(i)
        m1=t[i-1]
        q2,r=divmod(i,2)
        m2 = t[q2] if r==0 else sys.maxsize
        q3, r2 = divmod(i, 3)
        m3 = t[q3] if r2==0 else sys.maxsize
        mm=m1
        i-=1
        if m2<=mm:
            mm, i = m2, q2
        if m3<=mm:
            mm, i = m3, q3
    s.reverse()
    return s
input = sys.stdin.read()
n = int(input)
assert 1<=n<=10**6
table = minimum_calcs(n)
minimum_operations = table[n]
sequence = get_sequence(n)
print (minimum_operations)
for x in sequence:
    print(x, end=' ')
