# and, or, not, not le da el valor opuesto
gas = False
encendido = True
edad = 18

if gas and encendido and edad > 17:
    print("Puedes avanzar")
if not gas and encendido and edad > 17:  # primero los paréntesis, de normal es de izquierda a derecha
    print("Puedes avanzar")

edad = 25

if 15 <= edad <= 65:
    print("Tiene acesso a la piscina")
