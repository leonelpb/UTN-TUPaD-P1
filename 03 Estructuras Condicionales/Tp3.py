
# 1)
def calcularMayoriaDeEdad():
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad")

# 2)
def determinarAprobado():
    nota = float(input("Ingrese su calificacion: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")
        
# 3)
def determinarPar():
    numero = int(input("Ingrese un número par: "))
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

# 4)
def definirEtapaDeVida():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Niño/a")
    elif 12 <= edad < 18:
        print("Adolescente")
    elif 18 <= edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

# 5)
def ingresarContraseña():
    contrasena = input("Ingrese una contraseña: ")
    if 8 <= len(contrasena) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6)
import random
from statistics import mode, median, mean


def calcularSesgos():
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)

    print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

    if media > mediana > moda:
        print("Sesgo positivo (a la derecha)")
    elif media < mediana < moda:
        print("Sesgo negativo (a la izquierda)")
    else:
        print("Sin sesgo")

# 7)
def clasificarString():
    texto = input("Ingrese una frase o palabra: ")
    if texto[-1].lower() in "aeiou":
        print(texto + "!")
    else:
        print(texto)

# 8)
def transformarString():
    nombre = input("Ingrese su nombre: ")
    opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra en mayúscula: ")

    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción inválida")

# 9)
def determinarMagnitudTerremoto():
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve")
    elif 3 <= magnitud < 4:
        print("Leve")
    elif 4 <= magnitud < 5:
        print("Moderado")
    elif 5 <= magnitud < 6:
        print("Fuerte")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")

# 10)
def determinarEstacionDelAño():
    hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
    mes = input("Ingrese el mes del año (ej. marzo): ").lower()
    dia = int(input("Ingrese el día del mes: "))

    # Convertir mes a número
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
        "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
        "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    m = meses.get(mes, 0)

    # Clasificar la estación
    if (m == 12 and dia >= 21) or (1 <= m <= 2) or (m == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif (m == 3 and dia >= 21) or (4 <= m <= 5) or (m == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
    elif (m == 6 and dia >= 21) or (7 <= m <= 8) or (m == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    elif (m == 9 and dia >= 21) or (10 <= m <= 11) or (m == 12 and dia <= 20):
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
    else:
        estacion = "Fecha inválida"

    print(f"Estación: {estacion}")

def menuOpen():
    print("\nSeleccione una opción:")
    print("1 - Calcular Mayoria De Edad ")
    print("2 - Determinar Aprobado")
    print("3 - Determinar Si es Par o no")
    print("4 - Definir Etapa De Vida")
    print("5 - Ingresar Contraseña")
    print("6 - Calcular Sesgos")
    print("7 - Clasificar String")
    print("8 - Transformar String")
    print("9 - Determinar Magnitud Terremoto")
    print("10 - Determinar en que estacion se encuentra")
    print("0 - SALIR")

def main():
    while True:
        menuOpen()
        option = input("Ingrese una opcion ")

        match option:
            case "1":
                calcularMayoriaDeEdad()
            case "2":
                determinarAprobado()
            case "3":
                determinarPar()
            case "4":
                definirEtapaDeVida()
            case "5":
                ingresarContraseña()
            case "6":
                calcularSesgos()
            case "7":
                clasificarString()
            case "8":
                transformarString()
            case "9":
                determinarMagnitudTerremoto()
            case "10":
                determinarEstacionDelAño()
            case "0":
                print("¡Hasta luego")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
                

if __name__== "__main__":
    main()