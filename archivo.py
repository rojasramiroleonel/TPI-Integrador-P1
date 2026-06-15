def cargar_paises():

    paises = []

    try:

        archivo = open("TPI_Programacion1_RamiroRojas/paises.csv", "r")

        archivo.readline()

        for linea in archivo:

            datos = linea.strip().split(",")

            pais = {
                "nombre": datos[0],
                "poblacion": int(datos[1]),
                "superficie": int(datos[2]),
                "continente": datos[3]
            }

            paises.append(pais)

        archivo.close()

    except FileNotFoundError:
        print("No se encontró el archivo.")

    return paises


def guardar_paises(paises):

    archivo = open("TPI_Programacion1_RamiroRojas/paises.csv", "w")

    archivo.write("nombre,poblacion,superficie,continente\n")

    for pais in paises:

        linea = pais["nombre"] + "," + str(pais["poblacion"]) + "," + str(pais["superficie"]) + "," + pais["continente"] + "\n"

        archivo.write(linea)

    archivo.close()