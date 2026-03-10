# ============================================================
# ACTIVIDAD 3 - Cifrado César
# Python y Ciberseguridad
# ============================================================


# ------------------------------------------------------------
# PARTE 1: Función para cifrar una letra usando el Cifrado César
# ------------------------------------------------------------

def cifrar_letra(letra, desplazamiento):
    """
    Cifra una letra mayúscula usando el Cifrado César.
    
    Parámetros:
        letra (str): Un carácter en mayúscula (A-Z)
        desplazamiento (int): Número de posiciones a desplazar (1-25)
    
    Retorna:
        str: La letra cifrada
    """
    # Validamos que la letra sea una mayúscula y el desplazamiento esté en el rango correcto
    if desplazamiento < 1 or desplazamiento > 25:
        raise ValueError("El desplazamiento debe estar entre 1 y 25.")

    # Convertimos la letra a su posición numérica (0-25) usando ord() y restando 65
    # ord('A') = 65, por eso restamos 65
    posicion = ord(letra) - 65

    # Aplicamos el desplazamiento con módulo 26 para que sea circular (Z -> A)
    nueva_posicion = (posicion + desplazamiento) % 26

    # Convertimos de vuelta a letra sumando 65
    letra_cifrada = chr(nueva_posicion + 65)

    return letra_cifrada


# ------------------------------------------------------------
# PARTE 2: Funciones donde se cifran y descifran los mensajes completos
# ------------------------------------------------------------

def cifrar_mensaje(mensaje, desplazamiento):
    """
    Cifra un mensaje completo usando el Cifrado César.
    Solo cifra letras (A-Z); espacios, números y puntuación se mantienen igual.
    
    Parámetros:
        mensaje (str): El texto a cifrar
        desplazamiento (int): Número de posiciones a desplazar (1-25)
    
    Retorna:
        str: El mensaje cifrado
    """
    # Convertimos el mensaje a mayúsculas para uniformidad
    mensaje = mensaje.upper()

    mensaje_cifrado = ""

    # Recorremos cada carácter del mensaje
    for caracter in mensaje:
        if caracter.isalpha():
            # Si es una letra, la ciframos
            mensaje_cifrado += cifrar_letra(caracter, desplazamiento)
        else:
            # Si es espacio, número o puntuación, lo dejamos igual
            mensaje_cifrado += caracter

    return mensaje_cifrado


def descifrar_mensaje(mensaje_cifrado, desplazamiento):
    """
    Descifra un mensaje cifrado con César invirtiendo el desplazamiento.
    
    Parámetros:
        mensaje_cifrado (str): El texto cifrado
        desplazamiento (int): El mismo desplazamiento usado al cifrar
    
    Retorna:
        str: El mensaje original descifrado
    """
    # Descifrar es cifrar con el desplazamiento inverso (26 - desplazamiento)
    return cifrar_mensaje(mensaje_cifrado, 26 - desplazamiento)


# ------------------------------------------------------------
# PARTE 3: Programa principal para interactuar con el usuario
# ------------------------------------------------------------

def main():
    print("=" * 50)
    print("       CIFRADO CÉSAR - Python y Ciberseguridad")
    print("=" * 50)

    # Pedimos el mensaje al usuario
    mensaje = input("\nIntroduce el mensaje a cifrar: ")

    # Pedimos el desplazamiento con validación
    while True:
        try:
            desplazamiento = int(input("Introduce el desplazamiento (número entre 1 y 25): "))
            if 1 <= desplazamiento <= 25:
                break
            else:
                print("  ⚠ El desplazamiento debe estar entre 1 y 25. Inténtalo de nuevo.")
        except ValueError:
            print("  ⚠ Por favor, introduce un número entero válido.")

    # Ciframos el mensaje
    cifrado = cifrar_mensaje(mensaje, desplazamiento)
    print(f"\nMensaje original:  {mensaje.upper()}")
    print(f"Mensaje cifrado:   {cifrado}")

    # Desciframos para verificar que el proceso es correcto
    descifrado = descifrar_mensaje(cifrado, desplazamiento)
    print(f"Mensaje descifrado (verificación): {descifrado}")

    print("\n" + "=" * 50)


# Ejecutamos el programa principal
if __name__ == "__main__":
    main()