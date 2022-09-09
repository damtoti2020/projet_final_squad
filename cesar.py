print("bonjour tout le monde")
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
lowercase = 'abcdefghijklmnopqrstuvwyz'
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


#text = input("donne une phrase : ")
#pas = int(input("donne une pas : "))
cipherText = cesar_encript(' le code cesar est facile a dechifree', 12)

#phrase_encripte = cipherText(text, pas)
print(cipherText)
#print(phrase_encripte)

#phrase = input('entrer votre phrase à encriptée: ')
#pas = input('entrer votre pas: ')

#cesar_encript(phrase, str(pas))

# et pour dechiffer on a : cipherText = cesar_encript(' le code cesar est facile a dechifree', 12)
