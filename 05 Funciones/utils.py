# ========================
# ENTRADAS VALIDADAS
# ========================
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

# ===========================
# INTERFAZ DE USUARIO (SALIDA)
# ===========================
def saludar():
    """ Emite un saludo por consola en español """
    print("Hola...")

def despedir():
    print("Chau...")
