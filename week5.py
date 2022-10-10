q=int(input("Enter any prime number: "))
for r in range(1,q):
    s=[]
    for x in range(0,q-1): 
        s.append(r**x%q) 
    if(len(s)==len(set(s))):
        break 
print(r)
Xa=int(input("Enter private Xa :"))
Ya=r**Xa%q 
Xb=int(input("Enter private Xb :"))
Yb=r**Xb%q  

Ka=Yb**Xa%q 
Kb=Ya**Xb%q 
if(Ka==Kb):
    print("Key can be shared")
else:
    print("Key can't be shared")
