# - Los comentarios se escriben con "#"
#--------------------------------------

#Tipos de variables

cadena = "holiwis"
# - Las cadenas son conjuntos de caraceteres (string)

Entero = 1
# - Un número entero es un tipo de variable "int"

Booleano = True

Flotante = 3,45
#(Tupla)

print(type(Entero))
print(type(Booleano))
print(type(Flotante))
print(type(cadena))

#--------------------------------------

ComplejoA = 8 + 5j
ComplejoB = 6 + 3j

Resultado = ComplejoA + ComplejoB

print(Resultado)

Cadena1 = "Holi"

print(Cadena1+str(Entero))

#--------------------------------------

# Cada vez que una palabra va antes de un " = " la palabra pasa a ser un dato en si mismo

#--------------------------------------

Lista = [1,2,3,4,"hola",5]

Tupla = (1,"holasss",4,16,"adios")

Set = {1,2,3,"mundo",5,"hola"}

#--------------------------------------
#  IF Y ELSE:

variable = 20

if variable < 2:
    print("verdadero")
elif variable == 20:
    print("la variable es 20")
else:
    print("falso")

# el comando "elif" sólo se activará si no se cumplen los requisitos del "if" o el anterior "elif"

#--------------------------------------


#--------------------------------------
