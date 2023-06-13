def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado  # return detiene el for


print("chanchito")  # el depurador se detiene en esta linea
l = largo("Hola Mundo")
print(l)
