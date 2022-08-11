'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio8.py
Autor: ..............
Action: detecta numero negativos
'''
numero = int(input("Escriba un número: "))
if numero > 0:
    print(f"Ha escrito numero positivo {numero}")
elif numero < 0:
    print(f"Ha escrito numero negativo {numero}")
else:
    print(f"Ha escrito cero {numero}")
