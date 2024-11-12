# adivina
Explicación del Código
Este es un juego interactivo en el que el usuario debe adivinar un número generado aleatoriamente por el programa dentro del rango de 0 a 100. El programa le proporciona pistas para ayudarle a acercarse al número correcto, indicándole si su suposición es demasiado alta o demasiado baja. El objetivo es adivinar el número en la menor cantidad de intentos posibles.

Funcionamiento del Juego:
Generación del número aleatorio: El programa elige un número aleatorio entre 0 y 100 utilizando la función random.randint(0, 100).

Interacción con el usuario: El programa solicita al usuario que ingrese un número a través de la consola. Este número debe estar dentro del rango de 0 a 100, de lo contrario, se le pedirá que ingrese un número válido.

Pistas para adivinar: Si el número ingresado por el usuario es mayor que el número aleatorio, el programa le indicará que intente con un número más bajo. Si el número ingresado es menor que el número correcto, se le sugerirá intentar con un número más alto.

Verificación del número: Si el usuario adivina el número correctamente, el juego terminará y el programa le felicitará por su logro.

Manejo de errores: El programa maneja posibles errores de entrada, como cuando el usuario ingresa un valor no numérico, y le pedirá que ingrese un número entero válido.

¿Cómo jugar?
Al iniciar el programa, se te indicará el objetivo del juego y el rango de números posibles.
Ingresa un número en la consola.
Recibirás una pista sobre si tu número es más alto o bajo que el número correcto.
Sigue intentándolo hasta adivinar el número correcto. El juego te felicitará una vez que lo hayas logrado.
Código:
El código se encuentra escrito en Python, utilizando la librería random para generar el número aleatorio y controlando el flujo del juego con un bucle while. Además, se utiliza un bloque try-except para manejar posibles errores de entrada.
