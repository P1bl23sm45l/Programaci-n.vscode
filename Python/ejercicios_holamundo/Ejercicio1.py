print("Bienvenidos a la calculadora")
print("Para salir escriba Salir")
print("Las operaciones son suma, multi, div y resta")
n1 = int(input("Ingresa numero:"))
while True:
    x = str(input("Ingresa operación:"))
    if x.lower() == "salir":
        break
    else:
        n2 = int(input("Ingrese siguiente numero:"))
        if x.lower() == "suma":
            n1 = n1 + n2
            print("El resultado sería", n1)
        if x.lower() == "resta":
            n1 = n1-n2
            print("El resultado sería", n1)
        if x.lower() == "multi":
            n1 = n1*n2
            print("El resultado sería", n1)
        if x.lower() == "div":
            n1 = n1/n2
            print("El resultado sería", n1)
