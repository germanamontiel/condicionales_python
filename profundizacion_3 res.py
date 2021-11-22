# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temp_1 = int(input("Ingrese valor de temperatura: "))
temp_2 = int(input("Ingrese valor de temperatura: "))
temp_3 = int(input("Ingrese valor de temperatura: "))

temp_max = 240
temp_med = 120
temp_min = 60

# Primer valor

if temp_1 >= temp_max:
    print(temp_1, "es temperatura maxima")
elif temp_1 >= temp_med:
    print(temp_1, "es temperatura moderada")
elif temp_1 >= temp_min:
    print(temp_1, "es temperatura normal")
elif temp_1 >= 0:
    print(temp_1, "es una temperatura por debajo de lo normal")
else:
    print("ningun valor puede computarse")

# Segundo valor

if temp_2 >= temp_max:
    print(temp_2, "es temperatura maxima")
elif temp_2 >= temp_med:
    print(temp_2, "es temperatura moderada")
elif temp_2 >= temp_min:
    print(temp_2, "es temperatura normal")
elif temp_2 >= 0:
    print(temp_2, "es una temperatura por debajo de lo normal")
else:
    print("ningun valor puede computarse")

# Tercer valor

if temp_3 >= temp_max:
    print(temp_3, "es temperatura maxima")
elif temp_3 >= temp_med:
    print(temp_3, "es temperatura moderada")
elif temp_3 >= temp_min:
    print(temp_3, "es temperatura normal")
elif temp_3 >= 0:
    print(temp_3, "es una temperatura por debajo de lo normal")
else:
    print("ningun valor puede computarse")

# Promedio

if (temp_1 <= temp_max) or (temp_2 <= temp_med) or (temp_3 <= temp_min):
    promedio = (temp_1 + temp_2 + temp_3) /3
    print("El promedio de las temperaturas ingresadas es ", promedio)
else:
    print("Una de las temperaturas ingresadas\nno figura dentro del rango") 
