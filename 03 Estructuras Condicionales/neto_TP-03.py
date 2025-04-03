# 1) Solicita la edad del usuario y verifica si es mayor de 18 años.

edad = int(input("Escriba su edad: "))

if edad > 18:
    print("Es mayor de edad.")


# 2) Solicita la nota del usuario y determina si aprueba o desaprueba.

nota = float(input("Escriba su nota: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")


# 3) Solicita un número al usuario y verifica si es par.

numero = int(input("Escriba un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")


# 4) Solicita la edad del usuario y clasifica en categorías.

edad = int(input("Escriba su edad: "))

if edad < 12:
    print("Usted es niño/a.")
elif edad >= 12 and edad < 18:
    print("Usted es un adolescente.")
elif edad >= 18 and edad < 30:
    print("Usted es adulto/a joven.")
else:
    print("Usted es adulto/a.")


# 5) Solicita una contraseña y verifica su longitud.

contrasenia = input("Escriba una contraseña de entre 8 y 14 caracteres (incluyendo 8 y 14): ")

if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# 6) Genera una lista de números aleatorios y determina el sesgo en la distribución.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo.")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo.")
elif media == mediana == moda:
    print("No hay sesgo.")


# 7) Solicita una frase y añade un signo de exclamación si termina en vocal.

expresion = input("Escriba una frase o palabra: ")
ultimo_caracter = expresion[-1].lower()

if ultimo_caracter == "a" or ultimo_caracter == "e" or ultimo_caracter == "i" or ultimo_caracter == "o" or ultimo_caracter == "u":
    print(f"{expresion}!")
else:
    print(expresion)


# 8) Solicita el nombre y aplica la transformación seleccionada.

nombre = input("Escriba su nombre: ")
opcion = input("""Elija una opción:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
""")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
else:
    print(nombre.title())


# 9) Solicita la magnitud de un terremoto y lo clasifica según la escala de Richter.

magnitud = float(input("Escriba la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")


# 10) Solicita información sobre hemisferio, mes y día para determinar la estación del año.

hemisferio = input("¿En cuál hemisferio se encuentra (N/S)? ")
mes = int(input("¿Qué mes del año es? "))
dia = int(input("¿Qué día es? "))
if hemisferio.upper()=="N":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio.upper() == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
print(f"Estacion: {estacion}")
