choice=int(input("enter 1.Encryption or 2.Decryption"))
if choice==1:
    plaintext=input()
    key=int(input())
    result=""
    for i in range(len(plaintext)):
        char=plaintext[i]
        if(char.isupper()):
            result+=chr((ord(char)+key-65)%26+65)
        else:
            result+=chr((ord(char)+key-97)%26+97)
    print(result)
else:
    plaintext=input()
    key=int(input())
    result=""
    for i in range(len(plaintext)):
        char=plaintext[i]
        if(char.isupper()):
            result+=chr((ord(char)-key-65)%26+65)
        else:
            result+=chr((ord(char)-key-97)%26+97)
    print(result)
    
