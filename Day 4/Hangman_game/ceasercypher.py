alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
a = str(input("Type 'encode' to encrypt and 'decode' to decrypt")).lower()



def encode():
    encoded = ""
    for i in word:
        for j in alphabets:
            if i == j:
              b =  alphabets.index(j)
              encoded = encoded + alphabets[b+shift]
    print(encoded)
                
                
def decode():
    decoded = ""
    for i in word:
        for j in alphabets:
            if i == j :
                b = alphabets.index(j)
                decoded = decoded + alphabets[b-shift]   
    print(decoded) 
        
        

    



if a == "encrypt":
    word = input("please enter the word you want to encrypt").lower()
    shift = int(input("how many digit shift you  want"))
    encode()
else:
    word = input("please enter the word you want to decrypt").lower()
    shift = int(input("how many digit shift you  want"))
    decode()






