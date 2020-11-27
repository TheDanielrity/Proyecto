import collections
texto = input("Introduce el texto a descifrar: \n")
abecedario = "abcdefghijklmnopqrstuvwxyz"
abcmayus = abecedario.upper()
descifrado = ""


frecuencia = collections.Counter(texto.lower())
letra_repetida = {}

for llave, valor in list(frecuencia.items()):
    if valor > 1:
        letra_repetida[llave] = valor
       
if " " in letra_repetida:
    del letra_repetida[" "]

lista = list(letra_repetida.keys())
lista2 = list(letra_repetida.values())
mayor = 0

for valor in letra_repetida.values():
    if valor > mayor:
        mayor = valor

letra_mayor_repetida =lista[lista2.index(mayor)]

desplazamiento = ord(letra_mayor_repetida) - ord("e")

#aquí estaba probando si el código iba bien
""" print(desplazamiento)
print(letra_mayor_repetida)
 print(lista2.index(mayor))


print(lista, lista2)
print(mayor)
print(letra_repetida)  """


for letra in texto:
    if letra.isalpha():
        if letra in abcmayus:
            descifrado+=abcmayus[(abcmayus.index(letra))-desplazamiento%26]

        else:
            descifrado+=abecedario[(abecedario.index(letra))-desplazamiento%26] 
    else:
        descifrado+=letra 

print("Tu texto descifrado es:\n"+ descifrado, "\n\nLa llave de cifrado del texto es: ", desplazamiento)

