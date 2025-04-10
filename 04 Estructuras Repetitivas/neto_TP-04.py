# Trabajo Práctico - Unidad 4
# Autor: Franco Neto Aguirre
# Comisión: 18

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print("\nEjercicio 1\n")
for i in range(101):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

print("\nEjercicio 2\n")
numero_entero = input("Escriba un número entero: ")

while numero_entero == "" or numero_entero == " ":
    numero_entero = input("No ha escrito nada. Escriba un número entero: ")

cantidad_digitos = 0

for digito in numero_entero:
    if digito != "+" and digito != "-":
        cantidad_digitos += 1

print(f"Cantidad de dígitos que contiene {numero_entero}: {cantidad_digitos}")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

print("\nEjercicio 3\n")
limite_inferior = input("Escriba el límite inferior (debe ser un número entero): ")

while limite_inferior == "" or limite_inferior == " ":
    limite_inferior = input("No ha escrito nada. Escriba un número entero para el límite inferior: ")

limite_inferior = int(limite_inferior)
limite_superior = input("Escriba el límite superior (debe ser un número entero): ")

while limite_superior == "" or limite_superior == " ":
    limite_superior = input("No ha escrito nada. Escriba un número entero para el límite superior: ")

limite_superior = int(limite_superior)

while limite_inferior > limite_superior:
    print("Ha ingresado un límite inferior mayor que el superior. El límite inferior debe ser menor que el superior.")
    limite_inferior = input("Escriba de nuevo el límite inferior (debe ser un número entero): ")

    while limite_inferior == "" or limite_inferior == " ":
        limite_inferior = input("No ha escrito nada. Escriba un número entero para el límite inferior: ")

    limite_inferior = int(limite_inferior)

    limite_superior = input(f"Escriba de nuevo el límite superior (debe ser un número entero, y mayor o igual que {limite_inferior}): ")

    while limite_superior == "" or limite_superior == " ":
        limite_superior = input("No ha escrito nada. Escriba un número entero para el límite superior: ")

    limite_superior = int(limite_superior)

acumulador = 0

for i in range( (limite_inferior + 1), (limite_superior) ):
    acumulador += i

print(f"Suma de todos los números enteros comprendidos entre {limite_inferior} y {limite_superior}, excluyendo ambos valores: {acumulador}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("\nEjercicio 4\n")
FINALIZADOR = 0
numero_entero = input("Escriba un número entero (0 para terminar): ")

while numero_entero == "" or numero_entero == " ":
    numero_entero = input("No ha escrito nada. Escriba un número entero (0 para terminar): ")

numero_entero = int(numero_entero)
acumulador = 0

while numero_entero != FINALIZADOR:
    acumulador += numero_entero
    numero_entero = input("Escriba otro número entero (0 para terminar): ")

    while numero_entero == "" or numero_entero == " ":
        numero_entero = input("No ha escrito nada. Escriba un número entero (0 para terminar): ")

    numero_entero = int(numero_entero)


print(f"Total acumulado: {acumulador}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print("\nEjercicio 5\n")
import random

NUMERO_ALEATORIO = random.randint(0, 9)
numero_usuario = input("Adivine el número (de 0 a 9): ")

while numero_usuario == "" or numero_usuario == " ":
    numero_usuario = input("No ha escrito nada. Escriba un número entero (de 0 a 9): ")

numero_usuario = int(numero_usuario)

while numero_usuario < 0 or numero_usuario > 9:
    numero_usuario = input("Ha escrito un número que no está entre 0 y 9. Escriba un número entero de 0 a 9: ")

    while numero_usuario == "" or numero_usuario == " ":
        numero_usuario = input("No ha escrito nada. Escriba un número entero (de 0 a 9): ")

    numero_usuario = int(numero_usuario)

cantidad_intentos = 1

while NUMERO_ALEATORIO != numero_usuario:
    numero_usuario = input("¡Intente de nuevo! Ese no es el número: ")

    while numero_usuario == "" or numero_usuario == " ":
        numero_usuario = input("No ha escrito nada. Escriba un número entero (de 0 a 9): ")

    numero_usuario = int(numero_usuario)

    while numero_usuario < 0 or numero_usuario > 9:
        numero_usuario = input("Ha escrito un número que no está entre 0 y 9. Escriba un número entero de 0 a 9: ")

        while numero_usuario == "" or numero_usuario == " ":
            numero_usuario = input("No ha escrito nada. Escriba un número entero (de 0 a 9): ")

        numero_usuario = int(numero_usuario)

    cantidad_intentos += 1

print(f"¡Adivinó el número en {cantidad_intentos} intento(s)!")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

print("\nEjercicio 6\n")
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

print("\nEjercicio 7\n")
acumulador = 0
limite_superior = input("Escriba un número entero positivo: ")

while limite_superior == "" or limite_superior == " ":
    limite_superior = input("No ha escrito nada. Escriba un número entero positivo: ")

limite_superior = int(limite_superior)

while limite_superior <= 0:
    limite_superior = input("El número que ha escrito es cero o negativo. Escriba un entero positivo: ")

    while limite_superior == "" or limite_superior == " ":
        limite_superior = input("No ha escrito nada. Escriba un número entero positivo: ")

    limite_superior = int(limite_superior)

for i in range(limite_superior + 1):
    acumulador += i

print(f"Suma de todos los números comprendidos entre 0 y {limite_superior}: {acumulador}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("\nEjercicio 8\n")
limite_superior = 100
cantidad_pares = 0
cantidad_impares = 0
cantidad_positivos = 0
cantidad_negativos = 0

for i in range(1, (limite_superior + 1) ):
    numero_entero = input(f"Escriba el número entero nº {i} ({i}/{limite_superior}): ")

    while numero_entero == "" or numero_entero == " ":
        numero_entero = input("No ha escrito nada. Escriba un número entero: ")

    numero_entero = int(numero_entero)

    # Si un número entero no es par, entonces necesariamente es impar. Por lo tanto, usar un 'else' es suficiente.
    if numero_entero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

    # Dado que solo se deben considerar los números negativos, entonces es necesario usar un 'elif' junto a la condición correspondiente, sin considerar al cero.
    if numero_entero > 0:
        cantidad_positivos += 1
    elif numero_entero < 0:
        cantidad_negativos += 1

print(f"""Cantidad de números:
Pares: {cantidad_pares}
Impares: {cantidad_impares}
Positivos: {cantidad_positivos}
Negativos: {cantidad_negativos}
""")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

print("\nEjercicio 9\n")
limite_superior = 100
acumulador = 0
contador = 0

for i in range(1, (limite_superior + 1) ):
    numero_entero = input(f"Escriba el número entero nº {i} ({i}/{limite_superior}): ")

    while numero_entero == "" or numero_entero == " ":
        numero_entero = input("No ha escrito nada. Escriba un número entero: ")

    numero_entero = int(numero_entero)

    acumulador += numero_entero
    contador += 1

print(f"Promedio: {round( (acumulador / contador), 2)}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("\nEjercicio 10\n")
numero_entero = input("Escriba un número entero: ")

while numero_entero == "" or numero_entero == " ":
    numero_entero = input("No ha escrito nada. Escriba un número entero: ")

numero_invertido = ""

# Para invertir los dígitos, recorremos el string al revés. Desde el último índice hasta el primero, con paso -1.

for i in range( (len(numero_entero) - 1), -1, -1):
    if numero_entero[i] != "+" and numero_entero[i] != "-":
        numero_invertido += numero_entero[i]

if numero_entero[0] == "-":
    print(f"-{numero_invertido}")
else:
    print(numero_invertido)
