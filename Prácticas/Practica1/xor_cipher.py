#Funcion que cifra el texto recibido como
#parametro.
#Parametros: message,el texto encriptado
#que se quiere cifrar.
def cipher(message):
    arrays = list()
    for c in range(len(message)):
        arrays.append(chr(ord(message[c])^1))
    return ''.join(arrays)

#Funcion que descifra el texto recibido como
#parametro.
#Parametros: criptotext,el texto encriptado
#que se quiere descifrar.
def decipher(criptotext):
    arrays = list()
    for c in range(len(criptotext)):
        arrays.append(chr(ord(criptotext[c])^1))
    return ''.join(arrays)
