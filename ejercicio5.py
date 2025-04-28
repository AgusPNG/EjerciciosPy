def ejercicio():

    h = int(input("Horas: "))
    m = int(input("Minutos: "))
    s = int(input("Segundos: "))
    
    print("Horas: ",h,", minutos:",m,", segundos:",s,", segundos totales:",(((h*60)+m)*60)+s)
    
ejercicio()