def decode(inp):
    cipher=""
    for ch in inp:
        if not ch.isalpha():
            continue
        char=ord(ch)-1
        cipher+=chr(char)
    swp=cipher.swapcase()
    print("Decoded: ",swp)
    return swp
    
def cipherMe(inp):
    swp=inp.swapcase()
    cipher=""
    for ch in swp:
        if not ch.isalpha():
            continue
        char=ord(ch)+1
        cipher+=chr(char)
    print("Ciphered: ",cipher)
    return cipher

inp=input("Enter your input: ")
decode(cipherMe(inp))
