########Codigo Adivinanza 
# Haremos un codigo de adivinanza  
# 1. La maquina elegira un numero al azar del 1 al 10 
# 2. Definimos cuantos intentos tiene el usuario para adivinar el numero que eligio la maquina
# 3. Pedimos al usuario que ingrese el numero que cree que es el acertado
# 4. Si el usuario acierta se le muestra el mensaje de felicitación
# 5. Si el usuario falla se vuelve a repetir lo anterior es decir se vuelve a ejecutar el while

import random
print(f"Bienvenido\\da al juego de adivinar el numero\nEs muy sencillo tienes un total de 5 intentos\nAdivina el numero antes de llegar a los 5 intentos, ten en cuenta que el número es entre en 1 y el 10")
print()

intentos = 5 #Definimos el numero de intentos que tendremos como maximo
contador_de_intentos = 0 #Este sera el contador donde mostraremos al usuario el numero de intentas que lleva
numero_a_adivinar = random.randint(1,10) #Con la funcion random randidt elegimos un numero al azar del 1 al 10

numero_usuario = int(input("Que numero crees que es introducelo: ")) #Le pedimos al usuario el numero
print()


#Definimos el bucle que sera nuestro main del codigo, basicamente si no se cumplen ningua de las dos condiciones
#Le seguira pidiendo al usuario el numero y seguira mostrando el numeros de intentos que lleva
while contador_de_intentos != intentos and numero_usuario != numero_a_adivinar:
    contador_de_intentos += 1
    print(f"Actualmente tienes {contador_de_intentos} intentos realizados")
    numero_usuario = int(input("Que numero crees que es introducelo: "))
    print()

#Cuando el usuario adivine el numero le mostrara el siguente print en caso contrario ira al else y le dira que ha fallado mostrando el nuero que era
if numero_usuario == numero_a_adivinar:
    print(f"Enhorabuena has acertado!\nEl numero es {numero_a_adivinar}\nHas acertado en el intento {contador_de_intentos}")
else:
    print(f"Lastima has fallado!\nEl numero era {numero_a_adivinar}")    
