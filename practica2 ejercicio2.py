print ("introducir coeficientes")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))

discriminante = b*b - 4*(a)*(c)

if discriminante == 0:
    print("las raices son reales e iguales")
else:
    if discriminante > 0:
        print("las raices son reales y diferentes")
    else:
        if discriminante < 0:
            print("las raices son complejas")
        
