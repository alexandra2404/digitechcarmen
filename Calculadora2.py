#Creamos una variable boleana que sera lo que nos permitira entrar al while o salir 
#dependiendo de las opciones que marque el usuario
Salida = True

while Salida:
    print("--- Bienvenido/a a tu calculadora personal ---")
    print("="*50)
    print("Escoge opcion 1 para sumar (eje 1)")
    print("Escoge opcion 2 para restart (eje 2)")
    print("Escoge opcion 3 para multiplicar (eje 3)")
    print("Escoge opcion 4 para dividr (eje 4)")
    print("Escoge opcion 5 para calcular la potencia (eje 5)")
    print("Si dejas el espacio de las opciones en blanco o pones otro numero que no este en las opciones saldras de la calculadora")
    
    #Pedirmos la usuario que escoja una de las opciones que le hemos especificado
    opcion = input("Escoge una de las opciones: ")
    
    #Creamos una condicion donde verificamos que la opcion escojida por el usuario esta dentro de las opciones de las operaciones
    #en caso contrario saldra del bucle
    if opcion in ["1","2","3","4","5"]:
        try: # <--- Añadimos "try" para intentar leer los numeros
            numero1 = int(input("Introduce el primer numero: "))
            numero2 = int(input("Introduce el segundo numero: "))
        except ValueError: # <---- Si el usuario escribe "hola", esto captura el error
            print("\n¡Error! Debes introducir un número, no letras.Intentalo de nuevo.\n")
            continue # <----- "continue" se salta el resto y vuelve al inicio del "while Salida"
        
        # CAMBIAMOS EL 'else' PARA MANEJAR OPCIONES INVÁLIDAS
    elif opcion == "": # Si el usuario solo da Enter (como decías en tus instrucciones)
        print("Saliendo de la calculadora. ¡Adiós!")
        Salida = False # Esto sí cierra el programa
    else: # Si pone "7", "abc", o cualquier otra cosa
        print(f"\n¡Error! La opción '{opcion}' no es válida. Escoge del 1 al 5.\n")
        continue # 'continue' vuelve al inicio del 'while Salida' sin salirse
   

    #Dependiendo de la opcion que escoja el usuario haremos una condicion o otra 
    if opcion == "1":
        print(f"El resultado de la suma es: {numero1+numero2}")
    elif opcion == "2":
        print(f"El resultado de la resta es: {numero1-numero2}")
    elif opcion == "3":
        print(f"El resultado de la multiplicacion es: {numero1*numero2}")
    elif opcion == "4":
        print("Que clase de diviosn quieres hacer ?")
        print("="*50)
        print("Escoge opcion 1 para una division normal (eje 1)")
        print("Escoge opcion 2 para una division entera (eje 2)")
        print("Escoge opcion 3 para el resto de division (eje 3)")
        print("Si dejas el espacio de las opciones en blanco o pones otro numero que no este en las opciones saldras del calculo de divisiones")
        
        #Creamos otra variaable boleana que nos permite entrar en el bucle de las divisiones
        Salida_division = True
        
        while Salida_division:
            
            #Pedirmos la usuario que escoja una de las opciones que le hemos especificado
            opcion_division = input("Escoge una de las opciones para dividir: ")
            
            #Creamos una condicion donde verificamos que la opcion escojida por el usuario esta dentro de las opciones de las divisiones
            #en caso contrario saldra del bucle de las divisiones y seguira con el bucle principal
            if opcion_division in ["1","2","3"]:
                try: # <---- Añadimos "try"
                    numero1 = int(input("Introduce el primer numero: "))
                    numero2 = int(input("Introduce el segundo numero: "))
                except ValueError: # <--- Añadimos "except"
                    print("\n¡Error! Debes introducir un número. Intentalo de nuevo.\n")
                    continue # <---- "continue" vuelve al inicio del "while Salida_división"
            else:
                Salida_division = False
                continue # <--- AÑADIMOS "continue" para que no ejecute el codigo de abajo
            
            #Creamos un while donde dependiendo si el numero es igual a 0 seguira entrando hasta que el usuario ponga un numero diferente
            #Asi evitamos el error de la division por 0
            while numero2 == 0:
                print("No puedes dividir entre 0. pon otro numero.")
                try: # Añadimos Try
                    numero2 = int(input("Introduce el segundo numero: "))
                except ValueError: # <--- AÑADIMOS "except"
                    print("\n¡Error! Debes introducir un número. \n")
                    # No ponemos "continuar" para que el "while numero 2 == 0" no se repita
                
            #Dependiendo de la opcion que escoja el usuario haremos una condicion o otra 
            if opcion_division == "1":
                print(f"El resultado de la division normal es: {numero1/numero2}",end="\n")
            elif opcion_division == "2":
                print(f"El resultado de la division entera es: {numero1//numero2}",end="\n")
            elif opcion_division == "3":
                print(f"El resultado de la resta de la division es: {numero1%numero2}",end="\n")
            
            #Una vez nos haya dado el resultado finalizamos el bucle y volvemos al bucle principal
            Salida_division = False
            
    elif opcion == "5":
        print(f"El resultado de la potencia es: {numero1**numero2}",end="\n")