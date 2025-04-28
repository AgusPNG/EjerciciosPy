def ejercicio():
    
    f = int(input("Fecha (DDMMAAAA): "))
    
    print("Dia: ",int(f/1000000)," / Mes: ",int(f/10000)-int(f/1000000)*100," / Año: ",f-int(f/10000)*10000)
#                     16                        1600    -   1602 * 100                       16022008 - 1602,2008 * 10000
#                                               1600    -     160200                         16022008    -   16020000   
#                                                         2                                            2008

ejercicio()