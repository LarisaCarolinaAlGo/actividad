 # Lari
def cambio(matriz):
    cambio_1 = ""
    cambio_2 = ""
    cambio_3 = ""
    cambio_4 = ""

    lista_0 = matriz[0]
    palabra_0 = lista_0[0]
    palabra_1 = lista_0[1]
    lista_1 = matriz[1]
    palabra1_0 = lista_1[0]
    palabra1_1 = lista_1[1]
    for letra in palabra_0:
        if letra == "a":
            cambio_1 += "4"
        if letra == "e":
            cambio_1 += "3"
        if letra == "o":
            cambio_1 += "0"
        if letra == "u":
            cambio_1 += "v"
        if letra == "i":
            cambio_1 += "1"
        else:
            cambio_1 += letra

    # for letra in palabra_1:
    #     if letra == "a":
    #         cambio += "4"
    #     if letra == "e":
    #         cambio += "3"
    #     if letra == "o":
    #         cambio += "0"
    #     if letra == "u":
    #         cambio += "v"
    #     if letra == "i":
    #         cambio += "1"
    #     else:
    #         cambio += letra
    #
    # for letra in palabra1_0:
    #     if letra == "a":
    #         cambio += "4"
    #     if letra == "e":
    #         cambio += "3"
    #     if letra == "o":
    #         cambio += "0"
    #     if letra == "u":
    #         cambio += "v"
    #     if letra == "i":
    #         cambio += "1"
    #     elif letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
    #         cambio += letra
    #
    # for letra in palabra1_1:
    #     if letra == "a":
    #         cambio += "4"
    #     if letra == "e":
    #         cambio += "3"
    #     if letra == "o":
    #         cambio += "0"
    #     if letra == "u":
    #         cambio += "v"
    #     if letra == "i":
    #         cambio += "1"
    #     else:
    #         cambio += letra
    #
    return cambio_1

caja = [["hola", "adios"], ["vaselina", "bruja"]]

print(cambio(caja))
