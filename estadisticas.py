def estadisticas(paises):

    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    mayor = paises[0]
    menor = paises[0]

    suma_poblacion = 0
    suma_superficie = 0

    continentes = {}

    for pais in paises:

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\nPais con mayor poblacion:")
    print(mayor)

    print("\nPais con menor poblacion:")
    print(menor)

    print("\nPromedio de poblacion:")
    print(suma_poblacion / len(paises))

    print("\nPromedio de superficie:")
    print(suma_superficie / len(paises))

    print("\nCantidad de paises por continente:")

    for continente in continentes:
        print(continente, ":", continentes[continente])