import calculadora

resultado = calculadora.suma(30,45)
print(resultado)

try:
    print(2/0)
except Exception as ex:
    print("No es posible dividir entre cero")