import random

# Mensaje introductorio
print("\t#### ¡Adivina el Número! ####")
print("En este juego, deberás adivinar el número que el programa ha elegido al azar.")
print("El número está en el rango entre 0 y 100. ¡Muchísima suerte!")

# Generamos un número aleatorio entre 0 y 100
numero = random.randint(0, 100)
adivinado = False  # Variable para verificar si se ha adivinado el número

# Bucle que sigue hasta que el usuario adivine el número
while not adivinado:  
    try:
        # Solicitamos al usuario que ingrese un número
        numero_usuario = int(input("Introduce un número: "))
        
        # Verificamos que el número esté dentro del rango válido
        if 0 <= numero_usuario <= 100:  
            if numero_usuario == numero:  # Si el número es correcto, termina el juego
                adivinado = True
            elif numero_usuario > numero:  # Si el número ingresado es mayor que el correcto
                print("¡Demasiado alto! Intenta con un número más bajo.")
            else:  # Si el número ingresado es menor que el correcto
                print("¡Demasiado bajo! Prueba con un número más alto.")
        else:
            print("Por favor, ingresa un número dentro del rango entre 0 y 100.")
            
    except ValueError:  # Si el usuario ingresa algo que no es un número, le damos un mensaje
        print("Eso no es un número válido. Intenta de nuevo con un número entero.")

# Mensaje de felicitación una vez que el usuario adivina el número
print("¡Felicidades! Has adivinado el número correctamente.")
