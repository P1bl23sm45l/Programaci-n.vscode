def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="23",
            name="Iphone",
            desc="nave")  # nos arroja un diccionario.
# es necesario darle un nombre al parámetro. Podemos asignarle todos los argumentos que necesitemos
