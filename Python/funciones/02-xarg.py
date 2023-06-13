def suma(*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    print(resultado)


suma(2, 5, 7)  # iterables => for
suma(2, 5)
suma(2, 8, 7, 45, 32)
