def leap_year():
    text = int(input("Ingrese un año: "))
    resto = text%4
    cent = text%100
    cuat = text%400
    if resto==0:
        if cent == 0:
            if cuat == 0:  
                print(f"El año {text} es bisiesto")
            else:
                print(f"El año {text} no es bisiesto")
        else:
            print(f"El año {text} es bisiesto")
    else:
        print(f"El año {text} no es bisiesto") 
