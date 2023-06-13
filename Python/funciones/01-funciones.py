def hola(x, y="Feliz"):  # Muy importante los paréntesis, x e y son parametros
    print("Hola mundo")
    print(f"Bienvenido {x} {y}")


hola("nicolas", "Scuhurman")  # ahora es un argumento
# cuando no le demos valor al segundo parametro tomara el valor que le hayamos dado
hola("Pedro")

hola(y="schurman", x="nicolas")
