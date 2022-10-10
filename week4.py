def gcd(a,b):
    r=a%b
    if(r==0):
        return b
    else:
        return gcd(b,r)
p=int(input("enter prime number:"))
q=int(input("enter prime number:"))
me=int(input("enter message:"))
n=p*q
pi_n=(p-1)*(q-1)
print("pi_n:",pi_n)
e=2
while(e<pi_n):
    if(gcd(pi_n,e)==1):
        break
    e+=1
print("e:",e)
k=1
while(k>0):
    if((e*k)%(pi_n)==1):
        break
    k+=1
d=k
print("d:",d)
encrypt=pow(me,e)%n
print("Encryption:",encrypt)
decrypt=pow(encrypt,d)%n
print("Decryption",decrypt)


