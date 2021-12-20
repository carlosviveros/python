
def definir_orden(cad_a,cad_b,cad_C):
    return (sorted([cad_a,cad_b,cad_C]))

def ordenar_palabras():
    palabras = []
    while True:
        if len(palabras)==3:
            break
        palabra = input("ingrese una palabra > ")
        if palabra not in palabras:
            palabras.append(palabra)
        else:
            print(palabra," ya fue ingresada.")
    return palabras

palabras = ordenar_palabras()
palabras_ordenadas=definir_orden(palabras[0],palabras[1],palabras[2])
print(palabras_ordenadas)
