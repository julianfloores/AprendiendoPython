num1=input("Numero 1: ")
num2=input("Numero 2: ")
salida="Numeros proporcionados: {} y {}. {}."
if(num1==num2):
    print(salida.format(num1, num2, "Los numeros son iguales"))
else:
    if num1>num2:
        print(salida.format(num1, num2, "El mayor es el primero"))
    else:
        print(salida.format(num1, num2,  "El mayor es el segundo"))