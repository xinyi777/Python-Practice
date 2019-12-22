def func1(k,i):
    a=list(str(k))
    b=0
    for j in a:
        if int(j)<=i:
            b+=1

    return b

def func2(n):
    s=str(n)+'='
    dic={}
    while n>1:
        for i in range(2,n+1):
            if n%i==0:
                dic[i]=dic.get(i,0)+1
                n=n//i
                break
    a=sorted(dic.items(),key=lambda x:x[0])
    for i in a:
        s+=str(i[0])+"^"+str(i[1])+'*'

    return s[:-1]


def func3(lst,v):
    lst2=[]
    for i in lst:
        a=sum(int(j) for j in list(str(i)))
        if a<v:
            lst2.append(i)
    return sorted(lst2,reverse=True)



def func4(x):
    return len(set(list(str(x))))

def func5(lst):
    lst1=[]
    lst2=[]
    for i in lst:
        if i%2==0:
            lst2.append(i)
        else:
            lst1.append(i)
    newlst=sorted(lst1)+sorted(lst2,reverse=True)
    return newlst

def func6(s):
    import re
    import math
    lst=re.findall('(-?\d+,-?\d+)',s)
    lst2=[]
    for i in range(len(lst)):
        lst2.append(tuple(map(int,lst[i].split(','))))
    return sorted(lst2,key=lambda x:(math.sqrt(x[0]**2+x[1]**2),-x[1]))

def func7(s):
    lst=s.split()
    dic={}
    for i in lst:
        dic[i]=dic.get(i,0)+1
    b=sorted(dic.items(),key=lambda x:(x[1],x[0]),reverse=True)
    return [b[i][0] for i in range(len(b))][0:3]


if __name__=='__main__':
    # print(func3([1234, 2345, 5678, 8907],15))
    # print(func4(23389))
    # print(func6('(-3,4)(4,-3)(-4,-3)(3,4)'))
    # print(func7('hello hello hi apple'))
    pass
    #ps