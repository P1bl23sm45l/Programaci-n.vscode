numeros = [1, 2, 3]
# feo!
# primero =numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# con este metodo no podemos coger un único valor
primero, segundo, tercero = numeros
print(primero, segundo, tercero)
primero, *otros = numeros  # para el segundo elemento, es lo mismo
print(primero, otros)
primero, *otros, ultimo = numeros
print(primero, ultimo, otros)
