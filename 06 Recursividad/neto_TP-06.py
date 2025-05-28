from utils import factorial_recursivo, leer_int_validado

#1
numero_ingresado = leer_int_validado("Escriba un número entero: ", "Vuelva a intentar.")

for numero in range(1, numero_ingresado + 1):
    print(f"{numero}! = {factorial_recursivo(numero)}")

#2
posicion_ingresada = leer_int_validado("Escriba la posición: ", "Vuelva a intentar.")

def fibonacci(posicion):
    if posicion == 0 or posicion == 1:
        valor = posicion
    else:
        valor = fibonacci(posicion - 1) + fibonacci(posicion - 2)
    return valor

for posicion in range(0, posicion_ingresada + 1):
    print(fibonacci(posicion), end=", ")

#3
def calcular_potencia(n, m):
    if m == 0:
        potencia = 1
    else:
        potencia = n * calcular_potencia(n, m - 1)

    return potencia

print(calcular_potencia(2, 3))

#4
def decimal_a_binario(numero_base_decimal):
    cociente = numero_base_decimal // 2
    resto = numero_base_decimal % 2
    if cociente != 0:
        binario = decimal_a_binario(cociente) + str(resto)
    else:
        binario = str(resto)
    return binario

print(decimal_a_binario(10))

#5
def ver_si_es_palindromo(palabra):
    if len(palabra) >= 1:
        valor_inicio = palabra[0]
        valor_fin = palabra[-1]
        if valor_inicio != valor_fin:
            es_palindromo = False
        else:
            es_palindromo = ver_si_es_palindromo(palabra[1:len(palabra) - 1])
    else:
        es_palindromo = True
    return es_palindromo

print(ver_si_es_palindromo("anitalavalatina"))

#6
def suma_digitos(n):
    if n == 0:
        suma = 0
    else:
        digito = n % 10
        n //= 10
        suma = digito + suma_digitos(n)
    return suma

print(suma_digitos(305))

#7
def contar_bloques(n):
    if n == 1:
        contador_bloques = 1
    else:
        contador_bloques = n + contar_bloques(n - 1)
    return contador_bloques

print(contar_bloques(20))

#8
def contar_digito(numero, digito):
    digito_a = numero % 10
    if numero == 0 and digito != 0:
        contador_digitos = 0
    elif (digito_a == digito):
        contador_digitos = 1
        numero //= 10
        contador_digitos += contar_digito(numero, digito)
    else:
        contador_digitos = 0
        numero //= 10
        contador_digitos += contar_digito(numero, digito)
    return contador_digitos

print(contar_digito(7777777777, 7))
