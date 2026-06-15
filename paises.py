from archivo import *

def agregar_pais(paises):

    nombre = input("Nombre: ").strip()
    continente = input("Continente: ").strip()

    while nombre == "" or continente == "":
        print("No se permiten campos vacíos.")
        nombre = input("Nombre: ").strip()
        continente = input("Continente: ").strip()

    poblacion = int(input("Poblacion: "))
    superficie = int(input("Superficie: "))

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)

    guardar_paises(paises)

    print("Pais agregado correctamente.")


def actualizar_pais(paises):

    nombre = input("Ingrese el nombre del pais: ")

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            pais["poblacion"] = int(input("Nueva poblacion: "))
            pais["superficie"] = int(input("Nueva superficie: "))

            guardar_paises(paises)

            print("Pais actualizado.")
            return

    print("Pais no encontrado.")


def buscar_pais(paises):

    texto = input("Buscar pais: ").lower()

    encontrado = False

    for pais in paises:

        if texto in pais["nombre"].lower():

            print(pais)
            encontrado = True

    if encontrado == False:
        print("No se encontraron resultados.")


def filtrar_paises(paises):

    print("\n1. Continente")
    print("2. Rango de poblacion")
    print("3. Rango de superficie")

    opcion = input("Opcion: ")

    if opcion == "1":

        continente = input("Continente: ").lower()

        for pais in paises:

            if pais["continente"].lower() == continente:
                print(pais)

    elif opcion == "2":

        minimo = int(input("Poblacion minima: "))
        maximo = int(input("Poblacion maxima: "))

        for pais in paises:

            if pais["poblacion"] >= minimo and pais["poblacion"] <= maximo:
                print(pais)

    elif opcion == "3":

        minimo = int(input("Superficie minima: "))
        maximo = int(input("Superficie maxima: "))

        for pais in paises:

            if pais["superficie"] >= minimo and pais["superficie"] <= maximo:
                print(pais)

    else:
        print("Opcion invalida.")


def ordenar_paises(paises):

    print("\n1. Nombre")
    print("2. Poblacion")
    print("3. Superficie")

    opcion = input("Ordenar por: ")
    orden = input("A = Ascendente / D = Descendente: ").upper()

    lista = []

    if opcion == "1":

        for pais in paises:
            lista.append(pais["nombre"])

    elif opcion == "2":

        for pais in paises:
            lista.append(pais["poblacion"])

    elif opcion == "3":

        for pais in paises:
            lista.append(pais["superficie"])

    else:
        print("Opcion invalida.")
        return

    lista = sorted(lista)

    if orden == "D":
        lista.reverse()

    mostrados = []

    for valor in lista:

        for pais in paises:

            if pais in mostrados:
                continue

            if opcion == "1" and pais["nombre"] == valor:
                print(pais)
                mostrados.append(pais)

            elif opcion == "2" and pais["poblacion"] == valor:
                print(pais)
                mostrados.append(pais)

            elif opcion == "3" and pais["superficie"] == valor:
                print(pais)
                mostrados.append(pais)