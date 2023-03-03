import random  # importa random
import csv

palabras = int(input("¿De cuántas palabras desea que sea su contraseña? $ "))

lista = []

for i in range (0, palabras):
    
    dados = random.sample(range(1,7),5)  # genera 5 números entre 1 y 6

    numero = "".join(map(str,dados))  # convierte los 5 números en un string

    diccionario = {}  # genera un diccionario vacío

    with open('palabras1.csv', mode='r') as inp:  # abre el archivo csv
        reader = csv.reader(inp)  # toma inputs del csv
        diccionario = {rows[0]:rows[1] for rows in reader}  # toma inputs de cada columna
        
 
    
    lista.append(diccionario[numero])
    

resultado = ' '.join([str(elem) for elem in lista])

print(resultado)

