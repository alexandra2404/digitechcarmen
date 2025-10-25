"""
* Ahora crearemos nuestro código sobre música 
*************** CÓDIGO DE MUSICA****************
* * Este código calcula el tiempo total (en minutos y horas)que un 
* * usuario dedica a escuchar música. Pide al usuario su nombre,
* * cuántas canciones escucha al día y la duración promedio de esas canciones
* * Finalmente, determinaremos si es un "Melómano" basado en el tiempo
*
* VARIABLES Y CONSTANTES:
* --------------------------------------------------------------------
* * nombre_completo (variable, string): Almacena el nombre del usuario.
* * canciones (variable, string): Almacena la entrada de canciones (como texto).
* * tiempo (variable, string): Almacena la entrada de tiempo (como texto).
* * cantidad (variable, int): Número de canciones (convertido a entero).
* * tiem (variable, float): Duración promedio (convertido a decimal).
* * minuto_hora (constante, int): Valor fijo (60) usado para la conversión.
* * tiempo_total_minutos (variable, float): Resultado del cálculo aritmético (canciones * tiempo).
* * tiempo_total_horas (variable, float): Resultado de la conversión (minutos / 60).
*
""" 

print("Bievenido, vamos a descubrir que tanto amas la musica")


#Pedidmos informacion al usuario
nombre_completo = input("Cual es tu nombre completo: ")
canciones = input("Cuantas canciones escuchas al dia? (ej: 10): ")
tiempo = input("Cuanto tiempo suelen durar las canciones que escuchas? (ej: 3.5): ")



#Transformamos los datos de tiempo y canciones a enteros
cantidad = int(canciones)
tiem = float(tiempo)

#Creamos una constante que usuaremos mas adelante para nuestras operaciones
minuto_hora = 60

#Calculamos el tiempo de horas que el usuario pasa al dia escuchando musica
total_minutos = cantidad * tiem
total_horas = total_minutos / minuto_hora

print(f"\n--- Resumen para {nombre_completo} ---")
print(f"Escuchas un total de {total_minutos:.2f} minutos de música al día.")
print(f"¡Eso son {total_horas:.2f} horas diarias!")

#Creamos condiciones para saber si el usuario es melomano o no
if total_horas > 2:
    print("¡Disfrutas de una buena dosis de música diaria, eres un verdadero amante de la música!")
else:
    print("¡Disfrutas de la musica a tu ritmo!")









