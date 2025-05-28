from math import pi
from collections import deque

def leer_int_validado(mensaje, mensaje_error=None, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}"))
    while n < min or n > max:
        n = int(input(f"Error. {mensaje_error}"))
    return n


def leer_float_validado(mensaje, mensaje_error=None, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje}"))
    while n < min or n > max:
        n = float(input(f"Error. {mensaje_error}"))
    return n


def obtener_resto(num1, num2):
    return num1 - num2 * (num1 // num2) # Sin usar operador %


def es_multiplo(x, y):
    return obtener_resto(x, y) == 0


def siguiente(num):
    return num + 1


def doble(num):
    return num * 2


def calcular_area_circulo(radio):
    return pi * radio ** 2


def calcular_perimetro_circulo(radio):
    return 2 * pi * radio


def segundos_a_horas(segundos):
    return segundos / 3600


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    if b != 0:
        division = a / b
    else:
        division = None

    return (suma, resta, multiplicacion, division)


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def calcular_promedio(a, b, c):
    return (a + b + c) / 3


def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area


def calcular_precio_final(precio, descuento=0):
    precio_final = precio - (precio * descuento / 100)
    return round(precio_final, 2)


def es_primo(numero):
    """
        Retorna si un número natural es primo o no

        Parámetros
        ----------
        numero
            Un número natural a evaluar
        
        Retorna
        ----------
        Retorna True si el número resulta primo o coprimo
    """
    cont = 2
    mitad = numero // 2
    while cont <= mitad and not es_multiplo(numero, cont):
        cont += 1
    return cont > mitad


def sumatoria_divisores_propios(numero):
    sumatoria = 0
    for i in range(1, numero // 2 + 1):
        if es_multiplo(numero, i):
            sumatoria += i
    return sumatoria


def es_perfecto(numero):
    # Algunos nums perfectos: 6, 28, 496, 8128
    return sumatoria_divisores_propios(numero) == numero


def sucesion_simbolos(simbolo, veces):
    sucesion = ""
    for i in range(veces):
        sucesion += simbolo # sucesion = sucesion + simbolo
    return sucesion


def informar_si_numero_es_primo(numero):
    if es_primo(numero):
        print(f"El número {numero} es primo.")
    else: 
        print(f"El número {numero} no es primo.")


def informar_si_numero_es_perfecto(numero):
    if es_perfecto(numero):
        print(f"El número {numero} es perfecto.")
    else: 
        print(f"El número {numero} no es perfecto.")


def imprimir_simbolo(simbolo, veces):
    print( sucesion_simbolos(simbolo, veces) )


def imprimir_matriz_de_simbolos(nro_columnas, nro_filas, simbolo = "X"):
    for i in range(nro_filas):
        imprimir_simbolo(simbolo, nro_columnas)


def saludar():
    """ Emite un saludo por consola en español """
    print("Hola...")


def despedir():
    print("Chau...")


def tabla_multiplicar(n):
    lista = []
    for i in range(1, 11):
        lista.append(n * i)
    return lista


def suma_pares(numeros):
    suma = 0
    for num in numeros:
        if num % 2 == 0:
            suma += num
    return suma


def rectangulo(longitud, anchura):
    area = longitud * anchura
    perimetro = 2 * (longitud + anchura)
    return area, perimetro


def convertir_temperatura(celsius, unidad):
    if unidad == "F":
        return celsius * 9/5 + 32
    elif unidad == "K":
        return celsius + 273.15
    else:
        return "Unidad incorrecta"


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def promedio_calificaciones(calificaciones):
    total = 0
    for calif in calificaciones:
        total += calif
    return total / len(calificaciones)


def factorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado


def es_divisible(a, b):
    if b == 0:
        return False
    return a % b == 0


def convertir_a_fahrenheit(c):
    return c * 9/5 + 32


def convertir_a_kelvin(c):
    return c + 273.15


def menu_conversion():
    opcion = input("¿Convertir a (F)ahrenheit o (K)elvin? ")
    if opcion in ["F", "K"]:
        return opcion
    else:
        return None


def validar_dimensiones(longitud, anchura):
    return longitud > 0 and anchura > 0


def calcular_area(longitud, anchura):
    return longitud * anchura


def calcular_perimetro(longitud, anchura):
    return 2 * (longitud + anchura)


# Versión iterativa
def factorial(num):
    fact = 1
    for i in range(2, num):
        fact = fact * i
    return fact


# Funciones recursivas
def factorial_recursivo(num):
    if num == 0:
        fact = 1
    else:
        fact = num * factorial_recursivo(num - 1)
    return fact


def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])


def fibonacci(posicion):
    if posicion == 0 or posicion == 1:
        return posicion
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)


def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)


def repetir_frase(num, frase):
    if num >= 1:
        print(frase)
        repetir_frase(num - 1, frase)


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def sum_n_primos(num):
    if num==1:
        return 0
    elif es_primo(num):
        return num+sum_n_primos(num-1)
    else:
        return sum_n_primos(num-1)
