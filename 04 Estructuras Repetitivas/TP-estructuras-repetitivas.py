import random
import os # Para limpiar la pantalla, opcional

# --- Funciones de los ejercicios ---

def ejercicio_1():
    """Imprime números del 0 al 100."""
    print("\n--- Ejercicio 1: Números del 0 al 100 ---")
    for numero in range(101):
        print(numero)
    input("\nPresiona Enter para continuar...")

def ejercicio_2():
    """Determina la cantidad de dígitos de un número."""
    print("\n--- Ejercicio 2: Contar dígitos de un número ---")
    while True:
        try:
            numero_str = input("Ingresa un número entero: ")
            # Intentamos convertir a entero para validar que es un número
            int(numero_str)
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    cantidad_digitos = len(numero_str.lstrip('-')) # Elimina el signo negativo si existe
    print(f"El número {numero_str} tiene {cantidad_digitos} dígitos.")
    input("\nPresiona Enter para continuar...")

def ejercicio_3():
    """Suma números entre dos valores dados (excluyendo extremos)."""
    print("\n--- Ejercicio 3: Sumar entre dos valores (excluyendo extremos) ---")
    while True:
        try:
            valor1 = int(input("Ingresa el primer número entero: "))
            valor2 = int(input("Ingresa el segundo número entero: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa números enteros.")

    if valor1 > valor2:
        valor1, valor2 = valor2, valor1

    suma = 0
    for numero in range(valor1 + 1, valor2):
        suma += numero

    if suma == 0 and (valor2 - valor1 <= 1):
        print(f"No hay números enteros entre {valor1} y {valor2} para sumar (excluyendo los extremos).")
    else:
        print(f"La suma de los números enteros entre {valor1} y {valor2} (excluyendo los extremos) es: {suma}")
    input("\nPresiona Enter para continuar...")

def ejercicio_4():
    """Suma números ingresados hasta que se ingrese 0."""
    print("\n--- Ejercicio 4: Sumar números hasta 0 ---")
    total_acumulado = 0
    print("Ingresa números enteros para sumarlos. Ingresa 0 para finalizar y ver el total.")

    while True:
        try:
            numero = int(input("Ingresa un número (0 para terminar): "))
            if numero == 0:
                break
            total_acumulado += numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    print(f"El total acumulado es: {total_acumulado}")
    input("\nPresiona Enter para continuar...")

def ejercicio_5():
    """Juego de adivinar un número aleatorio."""
    print("\n--- Ejercicio 5: Juego de adivinar un número ---")
    numero_secreto = random.randint(0, 9)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 0 y 9. ¡Intenta adivinarlo!")

    while not adivinado:
        try:
            intento_usuario = int(input("Tu suposición: "))
            intentos += 1

            if intento_usuario < 0 or intento_usuario > 9:
                print("El número debe estar entre 0 y 9. Intenta de nuevo.")
            elif intento_usuario < numero_secreto:
                print("Demasiado bajo. ¡Intenta de nuevo!")
            elif intento_usuario > numero_secreto:
                print("Demasiado alto. ¡Intenta de nuevo!")
            else:
                adivinado = True
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
    input("\nPresiona Enter para continuar...")

def ejercicio_6():
    """Imprime números pares del 0 al 100 en orden decreciente."""
    print("\n--- Ejercicio 6: Números pares del 0 al 100 (decreciente) ---")
    for numero in range(100, -1, -2):
        print(numero)
    input("\nPresiona Enter para continuar...")

def ejercicio_7():
    """Calcula la suma de números entre 0 y un número positivo dado."""
    print("\n--- Ejercicio 7: Sumar números entre 0 y N ---")
    while True:
        try:
            limite = int(input("Ingresa un número entero positivo para calcular la suma desde 0: "))
            if limite < 0:
                print("Por favor, ingresa un número positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    suma = 0
    for numero in range(limite + 1):
        suma += numero

    print(f"La suma de todos los números entre 0 y {limite} es: {suma}")
    input("\nPresiona Enter para continuar...")

def ejercicio_8():
    """Clasifica 100 números enteros (pares/impares, positivos/negativos)."""
    print("\n--- Ejercicio 8: Clasificación de números ---")
    CANTIDAD_NUMEROS = 5 # Puedes cambiar a 100 para la versión final
    
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    ceros = 0

    print(f"Por favor, ingresa {CANTIDAD_NUMEROS} números enteros:")

    for i in range(CANTIDAD_NUMEROS):
        while True:
            try:
                numero = int(input(f"Ingresa el número {i + 1}: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1

    print("\n--- Resultados ---")
    print(f"Números ingresados: {CANTIDAD_NUMEROS}")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")
    print(f"Cantidad de números positivos: {positivos}")
    print(f"Cantidad de números negativos: {negativos}")
    print(f"Cantidad de ceros: {ceros}")
    input("\nPresiona Enter para continuar...")

def ejercicio_9():
    """Calcula la media de 100 números enteros."""
    print("\n--- Ejercicio 9: Calcular la media de N números ---")
    CANTIDAD_NUMEROS = 5 # Puedes cambiar a 100 para la versión final
    
    suma_total = 0
    print(f"Por favor, ingresa {CANTIDAD_NUMEROS} números enteros para calcular su media:")

    for i in range(CANTIDAD_NUMEROS):
        while True:
            try:
                numero = int(input(f"Ingresa el número {i + 1}: "))
                suma_total += numero
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
    
    if CANTIDAD_NUMEROS > 0:
        media = suma_total / CANTIDAD_NUMEROS
        print(f"\nLa suma total de los números es: {suma_total}")
        print(f"La media de los {CANTIDAD_NUMEROS} números ingresados es: {media:.2f}")
    else:
        print("No se ingresaron números, por lo tanto no se puede calcular la media.")
    input("\nPresiona Enter para continuar...")

def ejercicio_10():
    """Invierte el orden de los dígitos de un número."""
    print("\n--- Ejercicio 10: Invertir dígitos de un número ---")
    while True:
        try:
            numero_str = input("Ingresa un número entero para invertir sus dígitos: ")
            # Intentamos convertir a entero para validar que la entrada es numérica
            int(numero_str)
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
    
    numero_invertido_str = numero_str[::-1]
    print(f"El número {numero_str} invertido es: {numero_invertido_str}")
    input("\nPresiona Enter para continuar...")

# --- Funciones del menú ---

def limpiar_pantalla():
    """Limpia la consola."""
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para macOS y Linux
    else:
        os.system('clear')

def mostrar_menu():
    """Muestra las opciones del menú."""
    limpiar_pantalla()
    print("=" * 40)
    print("         MENÚ DE EJERCICIOS PYTHON")
    print("=" * 40)
    print(" 1. Números del 0 al 100")
    print(" 2. Contar dígitos de un número")
    print(" 3. Sumar entre dos valores (excluyendo extremos)")
    print(" 4. Sumar números hasta 0")
    print(" 5. Juego de adivinar un número")
    print(" 6. Números pares del 0 al 100 (decreciente)")
    print(" 7. Sumar números entre 0 y N")
    print(" 8. Clasificación de números (pares/impares, positivos/negativos)")
    print(" 9. Calcular la media de N números")
    print(" 10. Invertir dígitos de un número")
    print("-" * 40)
    print(" 0. Salir del programa")
    print("=" * 40)

def obtener_opcion_usuario():
    """Solicita y valida la opción del usuario."""
    while True:
        opcion = input("Selecciona una opción (0-10): ")
        try:
            opcion = int(opcion)
            if 0 <= opcion <= 10:
                return opcion
            else:
                print("Opción fuera de rango. Por favor, ingresa un número entre 0 y 10.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

# --- Programa Principal ---

def main():
    """Función principal para ejecutar el menú."""
    
    # Diccionario que mapea la opción a la función del ejercicio
    opciones = {
        1: ejercicio_1,
        2: ejercicio_2,
        3: ejercicio_3,
        4: ejercicio_4,
        5: ejercicio_5,
        6: ejercicio_6,
        7: ejercicio_7,
        8: ejercicio_8,
        9: ejercicio_9,
        10: ejercicio_10
    }

    while True:
        mostrar_menu()
        opcion_elegida = obtener_opcion_usuario()

        if opcion_elegida == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        elif opcion_elegida in opciones:
            # Ejecuta la función asociada a la opción elegida
            opciones[opcion_elegida]()
        else:
            # Esto no debería ocurrir si obtener_opcion_usuario funciona correctamente
            print("Opción no reconocida. Intenta de nuevo.")

if __name__ == "__main__":
    main()