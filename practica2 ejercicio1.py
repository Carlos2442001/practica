x=int(input("introdusca tiempo en segundos: "))

print("introducir tiempo de tarea")

h=int(input("introducir hora: "))  
m=int(input("introducir minutos: "))
s=int(input("introducir segundos: "))

m=m*60
h=h*3600
z=s+m+h

y=x-z

if y>=0:
    print("se puede finalizar la tarea")
else:
        print("no se podra finalizar la tarea")
        
