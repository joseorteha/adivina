# Adivina el Número - Juego en Python

Este es un juego interactivo donde el usuario debe adivinar un número generado aleatoriamente por el programa dentro del rango de 0 a 100. El programa proporciona pistas para ayudar al usuario a acercarse al número correcto, indicándole si su suposición es mayor o menor que el número secreto. El objetivo es adivinar el número en la menor cantidad de intentos posibles.

## Funcionamiento del Juego

1. **Generación del número aleatorio:**
   - El programa selecciona un número aleatorio entre 0 y 100 utilizando la función `random.randint(0, 100)`.

2. **Interacción con el usuario:**
   - El programa solicita al usuario que ingrese un número. Este número debe estar dentro del rango de 0 a 100. Si el número ingresado está fuera de este rango, el programa pedirá que ingrese un número válido.

3. **Pistas para adivinar:**
   - Si el número ingresado por el usuario es mayor que el número aleatorio, el programa le dirá "¡Demasiado alto!" y le sugerirá intentar con un número más bajo.
   - Si el número ingresado es menor que el número correcto, el programa le indicará "¡Demasiado bajo!" y sugerirá probar con un número más alto.

4. **Verificación del número:**
   - Si el usuario adivina el número correctamente, el juego terminará y el programa felicitará al usuario por su logro.

5. **Manejo de errores:**
   - Si el usuario ingresa un valor que no es un número válido (por ejemplo, texto o caracteres no numéricos), el programa le notificará que ha ingresado un valor incorrecto y le pedirá que ingrese un número entero.

## ¿Cómo jugar?

1. Al iniciar el programa, se te indicará el objetivo del juego y el rango de números posibles.
2. Ingresa un número en la consola cuando el programa te lo pida.
3. Recibirás una pista sobre si tu número es más alto o bajo que el número correcto.
4. Sigue intentando hasta adivinar el número correcto. El programa te felicitará una vez que lo hayas logrado.

## Código

El código está escrito en Python, utilizando la librería `random` para generar el número aleatorio. Se emplea un bucle `while` para mantener el juego activo hasta que el usuario adivine correctamente, y un bloque `try-except` para manejar posibles errores de entrada.

```python
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
