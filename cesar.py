print("Bonjour Mesdames et Monsieur , voici l'algorithme de César ")
print('*' * 100)
print("                              LE CODE CESAR  ")
print('*' * 100)
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'

phrase = input('entrer votre phrase à encriptée: ')
pas = int(input('entrer votre pas: '))

def cesar_encript(clearText, step):
    cipherText = ''

    for letter in clearText:
        if letter in uppercase:
            index = uppercase.index(letter)
            letterEncrypted = uppercase[(index + step) % 26]
            cipherText += letterEncrypted
        elif letter in lowercase:
            index = lowercase.index(letter)
            letterEncrypted = lowercase[(index + step) % 26]
            cipherText += letterEncrypted
        elif letter == ' ':
            cipherText += ' '
    return cipherText

#cipherText = cesar_encript(' le code cesar est facile a dechifree', 12)
phrase_encripte = cesar_encript(phrase, pas)
#print(cipherText)
print(phrase_encripte)
#print(phrase_encripte)

#cesar_encript(phrase, str(pas))

# et pour dechiffer on a : cipherText = cesar_encript(' le code cesar est facile a dechifree', 12)
