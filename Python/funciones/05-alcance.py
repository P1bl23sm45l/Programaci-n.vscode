saludo = "Global"


def saludar():
    global saludo  # pesima practica
    saludo = "Hola"
    print(saludo)


def saludaChancho():
    saludo = "Hola Chancho"
    print(saludo)


resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2)
