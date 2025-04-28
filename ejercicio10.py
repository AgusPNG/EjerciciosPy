def ejercicio():
    
    examenes = int(input("Calificacion por examenes parciales (30%): "))
    tps = int(input("Calificacion por trabajos practicos (20%): "))
    examen_in = int(input("Calificacion por el examen integrador (50%): "))

    print("Nota A: ",examenes," Nota B: ",tps," Nota C: ",examen_in," Nota final: ",(examenes*0.3)+(tps*0.2)+(examen_in*0.5))
    
ejercicio()
