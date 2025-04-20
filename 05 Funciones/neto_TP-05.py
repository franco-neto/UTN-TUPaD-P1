from math import pi
from utils import (
    saludar,
    leer_int_validado,
    leer_float_validado,
    despedir
)

def imprimir_hola_mundo() -> None:
    """
    Imprime el mensaje "Hola Mundo!" en la consola.

    Returns:
        None
    """
    print("Hola Mundo!")


def saludar_usuario(nombre: str) -> str:
    """
    Genera un saludo personalizado para el usuario.

    Args:
        nombre (str): El nombre del usuario.

    Returns:
        str: Una cadena con el saludo "Hola {nombre}!".
    """
    return f"Hola {nombre}!"


def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
    """
    Imprime la información personal proporcionada.

    Args:
        nombre (str): Nombre de la persona.
        apellido (str): Apellido de la persona.
        edad (int): Edad de la persona en años.
        residencia (str): Lugar de residencia de la persona.

    Returns:
        None
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo a partir de su radio.

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El área del círculo, redondeada a dos decimales.
    """
    return round(pi * radio**2, 2)


def calcular_perimetro_circulo(radio: float) -> float:
    """
    Calcula el perímetro (circunferencia) de un círculo a partir de su radio.

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El perímetro del círculo, redondeado a dos decimales.
    """
    return round(2 * pi * radio, 2)


def segundos_a_horas(segundos: float) -> float:
    """
    Convierte una cantidad de segundos a horas.

    Args:
        segundos (float): Número de segundos.

    Returns:
        float: Equivalente en horas, redondeado a dos decimales.
    """
    return round(segundos / 3600, 2)


def tabla_multiplicar(numero: float) -> None:
    """
    Imprime la tabla de multiplicar del número dado de 1 a 10.

    Args:
        numero (float): El número cuya tabla se va a generar.

    Returns:
        None
    """
    for multiplicador in range(1, 11):
        multiplicacion = round(numero * multiplicador, 2)

        print(f"{numero} x {multiplicador} = {multiplicacion}")


def operaciones_basicas(a: float, b: float) -> tuple[str, str, str, str]:
    """
    Realiza operaciones aritméticas básicas entre dos números.

    Args:
        a (float): Primer operando.
        b (float): Segundo operando.

    Returns:
        Tuple[str, str, str, str]: Tupla con los resultados de la suma, resta, multiplicación y división (o "Indefinido" si b es cero), cada uno como cadena.
    """
    numeros_sumados = f"{a} + {b} = {round(a + b, 2)}"
    numeros_restados = f"{a} - {b} = {round(a - b, 2)}"
    numeros_multiplicados = f"{a} x {b} = {round(a * b, 2)}"
    if b != 0:
        numeros_divididos = f"{a} ÷ {b} = {round(a / b, 2)}"
    else:
        numeros_divididos = f"{a} ÷ {b} = Indefinido"
    return (numeros_sumados, numeros_restados, numeros_multiplicados, numeros_divididos)


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.

    Returns:
        float: El IMC, redondeado a dos decimales.
    """
    return round(peso / altura**2, 2)


def celsius_a_fahrenheit(celsius: float) -> float:
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.

    Args:
        celsius (float): Temperatura en grados Celsius.

    Returns:
        float: Temperatura en grados Fahrenheit, redondeada a dos decimales.
    """
    return round(9/5 * celsius + 32, 2)


def calcular_promedio(a: float, b: float, c: float) -> float:
    """
    Calcula el promedio de tres números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.
        c (float): Tercer número.

    Returns:
        float: Promedio de los tres números, redondeado a dos decimales.
    """
    return round((a + b + c) / 3, 2)


saludar()

# Ejercicio 1
print("""
==================================================
Ejercicio 1: Imprimir por pantalla: “Hola Mundo!”.
==================================================""")

imprimir_hola_mundo()

# Ejercicio 2
print("""
==============================================
Ejercicio 2: Devolver un saludo personalizado.
==============================================""")

nombre = input("Escriba su nombre: ")
saludo = saludar_usuario(nombre)

print(saludo)

# Ejercicio 3
print("""
===========================================
Ejercicio 3: Imprimir información personal.
===========================================""")

nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
edad = leer_int_validado(
    mensaje="Escriba su edad: ",
    mensaje_error="Su edad debe ser mayor o igual que 0. Reescriba su edad: ",
    min=0
)
residencia = input("¿Dónde vive usted? ")

informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4
print("""
=====================================================
Ejercicio 4: Calcular área y perímetro de un círculo.
=====================================================""")

radio = leer_float_validado(
    mensaje="Escriba el radio de un círculo: ",
    mensaje_error="El radio del círculo debe ser mayor o igual que 0. Reescriba el radio de un círculo: ",
    min=0
)
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# Ejercicio 5
print("""
===============================================================================================
Ejercicio 5: Recibir una cantidad de segundos y devolver la cantidad de horas correspondientes.
===============================================================================================""")

segundos = leer_float_validado(
    mensaje="Escriba una cantidad de segundos: ",
    mensaje_error="La cantidad de segundos debe ser mayor o igual que 0. Reescriba una cantidad de segundos: ",
    min=0
)
horas = segundos_a_horas(segundos)

print(f"{segundos} segundo(s) equivale a {horas} hora(s).")

# Ejercicio 6
print("""
=======================================================================
Ejercicio 6: Imprimir la tabla de multiplicar de un número del 1 al 10.
=======================================================================""")

numero = int(input("Escriba un número entero: "))

tabla_multiplicar(numero)

# Ejercicio 7
print("""
====================================================================================
Ejercicio 7: Recibir dos números y sumarlos, restarlos, multiplicarlos y dividirlos.
====================================================================================""")

primer_numero = float(input("Escriba un número: "))
segundo_numero = float(input("Escriba otro número: "))
resultados = operaciones_basicas(primer_numero, segundo_numero)

for resultado in resultados:
    print(resultado)

# Ejercicio 8
print("""
=======================================================
Ejercicio 8: Calcular el índice de masa corporal (IMC).
=======================================================""")

peso = leer_float_validado(
    mensaje="Escriba su peso en kilogramos: ",
    mensaje_error="Su peso debe ser mayor o igual que 0. Reescriba su peso en kilogramos: ",
    min=0
)
altura = float(input("Escriba su altura en metros: "))
while altura <= 0:
    altura = leer_float_validado(
        mensaje="Error. Su altura debe ser mayor que 0. Reescriba su altura en metros: ",
        mensaje_error="Su altura debe ser mayor que 0. Reescriba su altura en metros: "
)

imc = calcular_imc(peso, altura)

print(f"Tu índice de masa corporal (IMC) es: {imc}")

# Ejercicio 9
print("""
===============================================================================================
Ejercicio 9: Recibir una temperatura en grados Celsius y devolver su equivalente en Fahrenheit.
===============================================================================================""")

temperatura_en_celsius = leer_float_validado(
    mensaje="Escriba una temperatura en grados Celsius: ",
    mensaje_error="La temperatura en grados Celsius debe ser mayor o igual que -273.15. Reescriba una temperatura en grados Celsius: ",
    min=-273.15
)

temperatura_en_fahrenheit = celsius_a_fahrenheit(temperatura_en_celsius)

print(f"{temperatura_en_celsius} grado(s) Celsius equivale a {temperatura_en_fahrenheit} grado(s) Fahrenheit.")

# Ejercicio 10
print("""
===================================================
Ejercicio 10: Devolver el promedio de tres números.
===================================================""")

primer_numero = float(input("Escriba un número: "))
segundo_numero = float(input("Escriba otro número: "))
tercer_numero = float(input("Escriba el último número: "))

promedio = calcular_promedio(primer_numero, segundo_numero, tercer_numero)

print(f"El promedio de {primer_numero}, {segundo_numero} y {tercer_numero} es: {promedio}")

despedir()
