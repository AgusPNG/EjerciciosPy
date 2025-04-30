def ejercicio():
    
    autos = int(input("Autos vendidos: "))
    valores = [0]*autos
    salario = 0

    for n in range(0,autos):
        valores[n] = int(input("Valor del auto: "))
        salario += ((valores[n]*0.05)+200)

    print("Salario: ",int(5500+salario))

ejercicio()
