import random  # importa random
import csv

palabras = int(input("¿De cuántas palabras desea que sea su contraseña? $ "))

for i in range (0, palabras):
    
    dados = random.sample(range(1,7),5)  # genera 5 números entre 1 y 6

    numero = "".join(map(str,dados))  # convierte los 5 números en un string


    diccionario = {}

    with open('palabras1.csv', mode='r') as inp:
        reader = csv.reader(inp)
        diccionario = {rows[0]:rows[1] for rows in reader}


    print(diccionario[numero])