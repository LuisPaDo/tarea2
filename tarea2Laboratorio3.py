#EJERCICIO 1
numero= int (input ("ingrese su numero \n")) 

if numero %2 ==0:
    print ("El numero es par ")
else:
    print ("el numero es impar")
#Ejercicio 2
factura= int (input ("ingrese su factura \n")) 

if factura <10000:
    print ("no se le cobrara comison ")
else:
    factura2=(factura *5)/100
    print ("Se le cobrara comision de ", factura2) 
#ejercicio 3
print ("Las elecciones de mezcla de color son las siguientes : \n")
print ("1) Azul + verde = ? \n")
print ("2) Verde + rojo = ? \n")

color=int(input("Ingrese su eleccion de color \n")) 

if color == 1:
        print ("Su color es Cyan")
else:
    if color == 2:
        print("Su color es cafe")
    else:
        print("Numero no valido")
#ejercicio 4
nota1= int (input ("ingrese su primer nota  \n")) 
nota2= int (input ("ingrese su segunda nota  \n")) 
nota3= int (input ("ingrese su tercera nota  \n")) 
nota4= int (input ("ingrese su cuarta nota  \n")) 

promedio=  (nota1+nota2+nota3+nota4)/4

if 1<=promedio <=10:
     print ("su nota final es de ", promedio, "Promedio de F")
elif 11<= promedio <=20:
     print ("su nota final es de ", promedio, "Promedio de E")
elif 21<= promedio <=30:
     print ("su nota final es de ", promedio, "Promedio de D")
elif 31<= promedio <=40:
     print ("su nota final es de ", promedio, "Promedio de C")
elif 41<= promedio <=50:
     print ("su nota final es de ", promedio, "Promedio de B")
elif 51<= promedio <=100:
     print ("su nota final es de ", promedio, "Promedio de A")
else:
     print ("numero de calificacion fuera de rango, vuelva a intertarlo")