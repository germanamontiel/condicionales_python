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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero_1 = int(input("ingrese un numero: "))
numero_2 = int(input("ingrese otro numero: "))

# Primer numero

if numero_1 > 0:
    print(numero_1, "Es positivo")
elif numero_1 < 0:
    print(numero_1, "Es negativo")
elif numero_1 == 0:
    print(numero_1, "Es cero")
else:
    print("Segui pensando")

# Segundo numero

if numero_2 > 0:
    print(numero_2, "Es positivo")
elif numero_2 < 0:
    print(numero_2, "Es negativo")
elif numero_2 == 0:
    print(numero_2, "Es cero")
else:
    print("Segui pensando")
