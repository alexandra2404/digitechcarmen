
""" ACTIVIDAD 3 - Cifrado César

PARTE 1: Función para cifrar una letra usando el Cifrado César
"""
#Empezamos a hacer la definición
def cifrar_letra(letra, desplazamiento):
    """
    Cifra una letra mayúscula usando el Cifrado César.
    
    Parámetros:
        letra (str): Un carácter en mayúscula (A-Z)
        desplazamiento (int): Número de posiciones a desplazar (1-25)
    
    Regresaremos finalmente:
        str: La letra cifrada
    """
    # Aquí elegimos el rango de desplazamiento de las letras y si está fuera de este rango daremos el error de que el desplazamiento debe estar entre 1 y 25
    if desplazamiento < 1 or desplazamiento > 25:
        raise ValueError("El desplazamiento debe estar entre 1 y 25.")

    # Convertimos la letra a su posición numérica (0-25) usando ord() que lo convertira en codigo ascii y restando 65
    # ord('A') = 65, por eso restamos 65 porque lo hice con el codigo ascii
    posicion = ord(letra) - 65

    # Aplicamos el desplazamiento con módulo 26 para que sea circular (Z -> A) ya que si sobrepasa el numero con el resto volveremos a empezar el abecedario
    nueva_posicion = (posicion + desplazamiento) % 26

    # Convertimos de vuelta a letra con chr () y sumamos 65 para que vuelva a estar en el codigo ascii
    letra_cifrada = chr(nueva_posicion + 65)

    return letra_cifrada


# PARTE 2: Funciones donde se cifran y descifran los mensajes completos


def cifrar_mensaje(mensaje, desplazamiento):
    """
    Cifra un mensaje completo usando el Cifrado César.
    Solo cifra letras (A-Z); espacios, números y puntuación se mantienen igual.
    
    Parámetros:
        mensaje (str): El texto a cifrar
        desplazamiento (int): Número de posiciones a desplazar (1-25)
    
    Regresamos:
        str: El mensaje cifrado
        
    """
    # Convertimos el mensaje a mayúsculas con el .upper()
    mensaje = mensaje.upper()
#Dejamos el "" para aclarar que es una variable vacia y allí guardaremos las letras
    mensaje_cifrado = ""

    # Empezamos el bucle y  recorremos letra por letro  el mensaje
    for caracter in mensaje:
        if caracter.isalpha():
            # Si es una letra, la ciframos ya que el isapha verifica si es una letra o no 
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
    
    Regresamos:
        str: El mensaje original descifrado 
    """
    # Descifrar es cifrar con el desplazamiento inverso (26 - desplazamiento)
    return cifrar_mensaje(mensaje_cifrado, 26 - desplazamiento)


# PARTE 3: Programa para poner lo que mostraremos al usuario 


def main():
  
    print("       CIFRADO CÉSAR - Python y Ciberseguridad ^u^ ")
   

    # Pedimos el mensaje al usuario con el input
    mensaje = input("\nIntroduce el mensaje a cifrar: ")

    # Pedimos el desplazamiento con validación
    """Abrimos un While y pedimos al usuario introducir el desplazamiento que quiere 
    #Si el desplazamiento que introduce el usuario cumple con el rango que especificamos 
    Si está el usuario lo introdujo bien se rompe el bucle y se continua con el programa 
    Y si no lo introduce bien nos saltaria el mensaje de escribir dentro del rango del 1 qal 25 
    y sino nos pide introducir un numero valido 
    """
    while True:
        try:
            desplazamiento = int(input("Introduce el desplazamiento (número entre 1 y 25): "))
            if 1 <= desplazamiento <= 25:
                break
            else:
                print("   El desplazamiento debe estar entre 1 y 25. Inténtalo de nuevo.")
        except ValueError:
            print("   Por favor, introduce un número entero válido.")

    # Ciframos el mensaje
    """ 
    Al inicio llamamos a la función que creamos antes ejecutandolo con los datos que introdujo el usuario antes en el input 
    Y se guarda en la variable cifrado 
    """
    cifrado = cifrar_mensaje(mensaje, desplazamiento)
    print(f"\nMensaje original:  {mensaje.upper()}")
    print(f"Mensaje cifrado:   {cifrado}")

    # Desciframos para verificar que el proceso es correcto
    descifrado = descifrar_mensaje(cifrado, desplazamiento)
    print(f"Mensaje descifrado (verificación): {descifrado}")

if __name__ == "__main__":
    main()


