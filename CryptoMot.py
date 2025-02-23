def chiffrement_cesar(texte, decalage):
    texte_chiffre = ""
    for caractere in texte:
        if caractere.isalpha():  
            decalage_ascii = ord('A') if caractere.isupper() else ord('a')
            texte_chiffre += chr((ord(caractere) - decalage_ascii + decalage) % 26 + decalage_ascii)
        else:
            texte_chiffre += caractere
    return texte_chiffre

def dechiffrement_cesar(texte_chiffre, decalage):
    return chiffrement_cesar(texte_chiffre, -decalage)


texte_original = input("Entrez une Texte:")
decalage = 3
texte_chiffre = chiffrement_cesar(texte_original, decalage)
texte_dechiffre = dechiffrement_cesar(texte_chiffre, decalage)

print(f"Texte original: {texte_original}")
print(f"Texte chiffré: {texte_chiffre}")
print(f"Texte déchiffré: {texte_dechiffre}")