buscar = 7
for numero in range(5):  # iterable, como las listas y las tuplas.
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontrado")

for char in "Ultimate python":
    print(char)
