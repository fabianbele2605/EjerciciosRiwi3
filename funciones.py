# Como definir una funcion
print("//////////////////////////////////")
print()
def saludar():
    print("Hola a todos")
    
saludar()
saludar()
saludar()
print()
print("//////////////////////////////////")



#Uso de parametros y argumentos(en el ejemplo de la pgina hay errores)

# la funcion
print("///////////////////////////////////")
#este es solo un mensaje para identifiacr los resultados de la operacion 
print("funciones para sumar")
print()
def sumarNumeros(primerNumero, segundoNumero):
    total = primerNumero + segundoNumero
    print(f"el resultado de la suma es {total}")
    
sumarNumeros(7, 9)
sumarNumeros(8, 45)
sumarNumeros(15, 96)
print()
print("//////////////////////////////////////////")
print()
#este es solo un mensaje para identifiacr los resultados de la operacion 
print("Funciones para rectar")
print()
def rectarNumeros(primerNumero, segundoNumero):
    total = primerNumero - segundoNumero
    print(f"el resultado de la recta es {total:.2f}")
    
rectarNumeros(10, 5)
rectarNumeros(25, 10)
rectarNumeros(5, 4)

print()
print("//////////////////////////////////////////")
print()
#Ejemplo de parametros preterminados(hay error en el ejemplo de la pagina!)
print("//////////////////////////////////////////")
print()

print("/////////////////////////////////////////")
print("Resultados de la multipliacacion")
print()
def multiplicarNumeros(primerNumero, segundoNumero):
    total = primerNumero * segundoNumero
    print(f"el resultado de la multiplicacion es {total:.2f}")
    
multiplicarNumeros(10, 5)
multiplicarNumeros(5, 5)
multiplicarNumeros(2, 5)

def dividirNumeros(primerNumero, segundoNumero):
    total = primerNumero / segundoNumero
    print(f"el resultado de la division es {total:.2f}")
    
dividirNumeros(50, 10)
dividirNumeros(25, 2)
dividirNumeros(8, 2)

print()
print("///////////////////////////////////////////")
print()

def saludar(nombre="Mundo"):
    print(f"Hola, {nombre}!")
    
saludar()
saludar("Pedro")
print()
print("///////////////////////////////////////////")



#Funciones con retornos 
#suma:

def suma(a, b):
    return(a + b)

resultado = suma(5, 7)
print(resultado)

#Recta
def recta(a, b):
    return(a - b)

resultado = recta(15, 9)
print(resultado)

#Multiplicacion:
def multiplicacion(a, b):
    return(a * b)

resultado = multiplicacion(5, 10)
print(resultado)

#Division
def division(a, b):
    return(a / b)

resultado=(50 / 2)
print(resultado)

#Funciones anonimas(lambda)

doblar = lambda x:x *5
print(doblar(16))





