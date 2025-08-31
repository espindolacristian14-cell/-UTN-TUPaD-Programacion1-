# Práctico 3: Estructuras condicionales
1#	Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 
edad= int (input(f"ingrese su edad:"))
if edad > 18:
     print("es mayor de edad")
"fin"

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota= int(input(f"ingrese su nota"))
if nota >= 6: 
     print("aprobado")
else:
     print("desaprobado")
"fin"

#Escribir un programa que permita ingresar solo números pares.
usuario= int(input(f"ingrese un numero"))
if usuario % 2 == 0:
     print("numero par")
else:
     print("numero impar")
"fin"

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años. 
usuario= int(input(f"ingrese su edad:"))
if usuario < 12:
     print("niño/a menor")
elif 12 <= usuario < 18: 
     print("adolecente")
elif 18 <= usuario < 30:
     print("adulto/a joven")
else:
     print("adulto/a mayor")
"fin"

#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
contraseña= input("ingrese contraseña de entre 8 y 14 caracteres:")
if 8 <= len (contraseña) <= 14:
     print("a ingresado la contraseña correcta")
else:
     print("pofavor ingrese una contraseña entre 8 y 14 caracteres")
"fin"

#calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
import random
from statistics import mode,median,mean 

numeros_aleatorios= {random.randint (1,100) for i in range (50)}
moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)

print("numeros_aleatorios", numeros_aleatorios)
print("moda", moda)
print("mediana", mediana)
print("media", media)

if media > mediana > moda:
     print("hay sesgo positivo")
elif media < mediana < moda:
     print("negativo")
else:
     print("no hay sesgo")
"fin"     

#Escribir un programa que solicite una frase o palabra al usuario.
palabra= input("ingrese una frase o palabra") 
if palabra[-1].lower() in "aeiou":
     palabra += "!"
print("resultado:", palabra)
"fin"

#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3.
nombre= input("ingrese su nombre")
numero= int(input("ingrese su numero (1,2 o 3"))

if numero == 1:
     print("resultado:", nombre.upper())
elif numero == 2:
     print("resultado:", nombre.lower())
elif numero == 3:
     print("resultado:", nombre.title())
else:
     print("no valida. debe ser 1,2 o 3.")
"fin"

#Escribir un programa que pida al usuario la magnitud de un terremoto.
terremoto= float(input("ingrese la magnitud del terremoto:"))

if terremoto < 3:
     print("muy leve")
elif terremoto >= 3 and terremoto < 4:
     print("leve")
elif terremoto >= 4 and terremoto < 5:
     print("moderado")
elif terremoto >= 5 and terremoto < 6:
     print("fuerte")
elif terremoto >= 6 and terremoto < 7:
     print("muy fuerte")
else:
     print("extremo")
"fin"

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
hemisferio= input("ingrese hemisferio (s/n):")
mes= int(input("ingrese el mes (1/12):"))
dia= int(input("ingrese dia (1/31):"))

if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
     norte= "invierno"
     sur= "verano"
elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
     norte= "primavera"
     sur= "otoño"
elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
     norte= "verano"
     sur= "invierno"
elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20):
     norte= "otoño"
     sur= "primavera"
else:
     norte= "invalido"
     sur= "invalido"

if hemisferio == "n":
     print("la estacion es:", norte)
elif hemisferio == "s":
     print("la estacion es:", sur)
else:
     print("hemisferio invalido, ingrese n o s")
"fin"