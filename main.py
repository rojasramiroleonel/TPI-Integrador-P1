from archivo import *
from paises import *
from estadisticas import *

def mostrar_menu():

    print("\n===== MENU =====")
    print("1. Agregar pais")
    print("2. Actualizar pais")
    print("3. Buscar pais")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Estadisticas")
    print("0. Salir")


def main():
    
    paises = cargar_paises()

    opcion = ""

    while opcion != "0":

        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_paises(paises)

        elif opcion == "5":
            ordenar_paises(paises)

        elif opcion == "6":
            estadisticas(paises)

        elif opcion == "0":
            print("Programa finalizado.")

        else:
            print("Opcion invalida.")


main()