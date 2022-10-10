#hill cipher encryption

import numpy as np

txt=input("Enter the plain text ")
key=input("Enter the key ")

txt_matrix=[]
for i in txt:
    if(i.isupper()):
        txt_matrix.append(ord(i)-65)
    else:
        txt_matrix.append(ord(i)-97)

key_matrix=[]
t=[]
for i in key:
    if(i.isupper()):
        t.append(ord(i)-65)
    else:
        t.append(ord(i)-97)

    if(len(t)==len(txt_matrix)):
        key_matrix.append(t)
        t=[]

txt_matrix=np.array(txt_matrix)
key_matrix=np.array(key_matrix)

res=np.dot(key_matrix,txt_matrix)
cipher=""
for i in res:
    cipher+=chr((i%26)+65)

print("The cipher text is",cipher)


#hill cipher decryption

import numpy as np
from egcd import egcd

def matrix_mod_inv(matrix, modulus):

    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv


cip_txt=input("Enter the cipher text ")
key=input("Enter the key ")

txt_matrix=[]
for i in cip_txt:
    if(i.isupper()):
        txt_matrix.append(ord(i)-65)
    else:
        txt_matrix.append(ord(i)-97)

key_matrix=[]
t=[]
for i in key:
    if(i.isupper()):
        t.append(ord(i)-65)
    else:
        t.append(ord(i)-97)

    if(len(t)==len(txt_matrix)):
        key_matrix.append(t)
        t=[]

Kinv = matrix_mod_inv(key_matrix,26)
txt_matrix=np.array(txt_matrix)
Kinv=np.array(Kinv)

res=np.dot(Kinv,txt_matrix)
plain=""
for i in res:
    plain+=chr((i%26)+65)


print("The plain text is ",plain)
