acumulado=int(0)
numero=str("")

while True:
    numero=input("Dame un número entero: ")
    if numero=="":
        print("Vacío. Salida del programa.")
        break
    else:
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))