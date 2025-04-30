def ejercicio():
    
    autos = int(input("Autos vendidos: "))
    salario = 0

    for n in range(0,autos):
        salario += (int(input("Valor del auto:"))*0.05+200)

    print("Salario: ",int(5500+salario))

ejercicio()
