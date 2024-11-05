def ceasar(message, decalage, mode="chiffrer"):
    resultat = ""
    
    if mode == "dechiffrer":
        decalage = -decalage
    
    for char in message:
        if char.isalpha():  
            point_de_depart = ord('A') if char.isupper() else ord('a')
            nouvelle_position = (ord(char) - point_de_depart + decalage) % 26
            resultat += chr(point_de_depart + nouvelle_position)
        else:
            resultat += char 

    return resultat

message = "HELLO"  
decalage = 3         
mode = "chiffrer"   

print("Résultat :", ceasar(message, decalage, mode))

mode = "dechiffrer"  
print("Résultat déchiffré :", ceasar(ceasar(message, decalage, "chiffrer"), decalage, mode))

if __name__ == '__main__':
    ceasar('hello', 3, 'chiffrer' )