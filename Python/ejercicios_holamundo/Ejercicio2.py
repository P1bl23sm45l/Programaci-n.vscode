def es_palindromo(texto):
    texto_minuscula = texto.lower()
    nuevo_texto = ""
    for i in texto_minuscula:
        if i != " ":
            nuevo_texto += i
    texto_reves = nuevo_texto[::-1]
    return texto_reves == nuevo_texto


print(es_palindromo("Casa"))
