def ls(l):
    i=l[0]
    l.pop(0)
    l.append(i)
    return l

def xor(a,b):
    x=[]
    for i in range(len(a)):
        x.append(a[i]^b[i])
    return x

def func(key_1,IP):
    print("initial permutation - ",IP)
    l1=IP[:len(IP)//2]
    r1=IP[len(IP)//2:]
    print("left half",l1,"right half",r1)
    k=[]
    for i in EP:
        k.append(r1[i-1])
    print("after expanded permutation",k)
    
    k=xor(k,key_1)
    print("after xor operation with key",k)
    l=k[:len(k)//2]
    r=k[len(k)//2:]

    _S0=bin(S0[int(str(l[0])+str(l[3]),2)][int(str(l[1])+str(l[2]),2)])[2:]
    _S1=bin(S1[int(str(r[0])+str(r[3]),2)][int(str(r[1])+str(r[2]),2)])[2:]

    print("S boxes")
    print("S0",_S0,"S1",_S1)
    _S0=list(_S0)
    _S1=list(_S1)
    k1=_S0+_S1
    k1=list(k1)
    for i in range(len(k1)):
        k1[i]=int(k1[i])

    k=[]
    for i in P4:
        k.append(k1[i-1])
    print("after p4",k)
    k1=xor(k,l1)
    print("after xor with left half of IP",k1)

    k=k1+r1

    print("after combine",k)  
    return k 

#input 

key=[1,0,1,0,0,0,0,0,1,0]
P10=[3,5,2,7,4,10,1,9,8,6]
P8=[6,3,7,4,8,5,10,9]
IP=[2,6,3,1,4,8,5,7]
EP=[4,1,2,3,2,3,4,1]
P4=[2,4,3,1]
IP_inv=[4,1,3,5,7,2,8,6]

S0=[[1,0,3,2],
[3,2,1,0],
[0,2,1,3],
[3,1,3,2]]

S1=[[0,1,2,3],
[2,0,1,3],
[3,0,1,0],
[2,1,0,3]]

#plain_text
pt=[1,0,0,1,0,1,1,1]

#key_1 generation
k=[]
for i in P10:
    k.append(key[i-1])

k=(ls(k[:len(k)//2]))+(ls(k[len(k)//2:]))
key_1=[]
for i in P8:
    key_1.append(k[i-1])

print("key 1 generated",key_1)

#key_2 generation
k=(ls(k[:len(k)//2]))+(ls(k[len(k)//2:]))
k=(ls(k[:len(k)//2]))+(ls(k[len(k)//2:]))

key_2=[]
for i in P8:
    key_2.append(k[i-1])

print("key 2 generated",key_2)
print("entered 8-bit plain text",pt)

#initial permutation

k=[]
for i in IP:
    k.append(pt[i-1])
print()
print("For key-1")
k1=func(key_1,k)

k1=k1[len(k)//2:]+k1[:len(k)//2]
print("after switching",k1)
print()
print("For key-2")
k2=func(key_2,k1)

ans=[]
for i in IP_inv:
    ans.append(k2[i-1])

print("after inverse initial permutation",ans)
print("Final cipher text obtained ",ans)
