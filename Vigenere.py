'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
       VIGENERE TABLE!
       
    FOR SOLOLEARN USERS:
     user interface:
     1---encrypt
     2---decrypt
     3---note
     
     if 1:::  your message :
              your key:

     if 2::: your encrypted word:
             your key:
             
             
    eg:
    type this way:
    *****†""*""""""""""
    
    1
    hello
    sololearn
    
    ***************""""""""""


by Mohammad_AnsaH 
upvote if you like!

'''
X="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=[]

for n in range(26):
    a=X[n:26]+X[0:n]
    l.append(a)

index={}
for n in range(26):
    index.update({X[n]:n})

def end():
    x=input("try again?(yes/no):").lower()
    if x=="yes":
        start()
    elif x=="no":
        print("thank you!")
    else:
        print("GIVE A VALID INPUT!")
        end()



def scan(word):
    c=""
    x='''[]{}#%^^*+=_\|~<>€0987654321 £¥•- :;()$&@".,?!'''
    for char in word:
        if char not in x:
            c+=char
    return c



#table letter scanner

def f(x,y):
    x=int(x)
    y=int(y)
    return l[x][y]

#decrypter??????????????
def decrypt():
    msg=input("your encrypted word(without space):").upper()
    msg=scan(msg)
    key=input("your key:").upper()
    key=scan(key)
    
    length_msg=len(msg)
    key_length=len(key)
    key*=(length_msg//key_length)+1
    key=key[:length_msg]
    
    c=""
    
    k=[]
    
    for n in range(length_msg):
        k.append(index[key[n]])
    
    res=[]
        
    for n in range(length_msg):
        for i in range(26):
            if l[k[n]][i] == msg[n]:
                res.append(l[i][0])
                
    result="".join(res)    
    print("result is:",result)
    end()



#encrypter???????????????

def encrypt():
    msg=input("your message(without space):").upper()
    msg=scan(msg)
    key=input("your key:(without space)").upper()
    key=scan(key)
    print("\nnote: only alphabets can be encrypted with vigenere table!\n")
    
    length_msg=len(msg)
    key_length=len(key)
    key*=(length_msg//key_length)+1
    key=key[:length_msg]
    
    c=""
    
    m=[]
    k=[]
    
    for n in range(length_msg):
        m.append(index[msg[n]])
        k.append(index[key[n]])
        
    for n in range(length_msg):
        c+=f(m[n],k[n])
        
    print("result is:",c)
    end()

def start():
    print("^"*60)
    print("\n\nwelcome to VIGENERE TABLE ")
    print(" \nMAIN MENU \n1)--- encrypt \n 2)---decrypt\n 3)-----note for programmers\n \n \nby Mohammad_AnsaH ")
    print("*"*60)
    in_put=input(":")
    if in_put=="1":
        encrypt()
    elif in_put=="2":
        decrypt()
    elif in_put=="3":
        print("*"*60)
        print("this program contains user interface .\ncomment me if you want simpler version of vigenere table to program")
        print("*"*60)
        start()
    else:
        print("enter a valid input$\n\n")
        print("*"*60)
        start()
    
start()
