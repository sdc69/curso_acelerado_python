'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion/ejercicio1.py
Autor: Programador x
Action: asignación de variables
'''
c1 = 10
c2 = 8
c3 = 8
estado = "tabasco"
tiempo = 40
precio = 34.78
ciudad = 'Villahermosa'
promedio = (c1 + c2 + c3) / 3
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 2403000000
promedio_temperatura = 31.3
estados_cercanos = ['chiapas', 'campeche', 'veracruz']
productos_tabasco = ['cacao', 'coco', 'caña']
print(
    nombre_estado,
    " es un estado que ",
)
print("con ", estados_cercanos[0], "colinda al sur", "y")
print("Tiene una superficie de ", superficie)
print("y cuenta con una temperatura promedio de:  ", promedio_temperatura)
print("El estado produce productos como", productos_tabasco[0])
print("el promedio es:", promedio)
print("la longitud de la cadena, ciudad es: ", len(ciudad))
print("eltipode estado es: ", type(estado))
print("eltipode tiempo es: ", type(tiempo))
print("eltipode precio es: ", type(precio))
print("el redondeo es: ", round(25.8))
numbers = [3, 5, 6, 2]
print(sum(numbers))
print(min(numbers))
print(chr(65))
print(str.capitalize("villa"))
print(str.lower("VILLAHERMOSA"))