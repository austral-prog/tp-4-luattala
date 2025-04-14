def line():
    import math
    a= float(input("Ingrese el coeficiente A: "))
    b= float(input("Ingrese el coeficiente B: "))
    X1= float(input("Ingrese el coeficiente X1: "))
    X2= float(input("Ingrese el coeficiente X2: "))
    print(f'El coeficiente A de su ecuación de la recta es: {a}\nEl coeficiente B de su ecuación de la recta es: {b}\nEl coeficiente X1 de su ecuación de la recta es: {X1}\nEl coeficiente X2 de su ecuación de la recta es: {X2}\n')
    print("Para la siguiente ecuación:" +"\n"+"\t"f' Y = {a}X + {b}\n' )
    y1 = a*X1+b
    y2 = a*X2+b
    p1 = X1,y1
    p2 = X2,y2
    print("Dados los siguientes puntos:" +"\n"+"\t" f"P1 {p1}"+"\n"+"\t" f"P2 {p2}\n")
    d = math.dist(p1,p2)
    print(f"La distancia entre ellos es: {d}") 
