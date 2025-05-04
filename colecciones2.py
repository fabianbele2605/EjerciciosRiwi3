
#Diccionario

coder={
    "Nombre":"Fabian Beleño",
    "Edad":25,
    "Correo Electronico":"Fabianrobles321@outlook.com",
    "Numero de Telefono":3214764419,
    "Soltero":False,
    "Direccion":"Lucero-barranquilla"
    
}

#Modificar los valores de un diccionario

Carro={
    "marca":"Kia",
    "modelo":"Rio",
    "año": 2020,
    "color":"negro",
}

print(Carro["marca"])
Carro["marca"]= "Kia Picanto"
print(Carro["marca"])
Carro["Motor"]= "V8"
print(Carro["Motor"])
del Carro["año"]
Carro.pop("color")




#Metodos utiles de los diccionarios

#Keys()

usuario1={
    "Nombre":"Noah",
    "Apellido":"Beleño",
    "Sexo":"Masculino",
    "Edad":20,
    "Cuidad":"barranquilla",
    "Correo electronico":"Noah1326@gmail.com"
}

claves=list(usuario1.keys())
print(claves)

#Items
#("0-3" ,0:marca, 1:modelo, 2:año, 3:color) --- ("0-1", 0:marca, 1:Hyudai,)
# Ejemplo la primera [2] es la categoria y [1] es la referancia especifica 
Carro={
    "marca":"Hyundai",
    "modelo":"I10",
    "año":2009,
    "color":"Gris plata",
}

items = list(Carro.items())
print(items[1])

print(items[2][0])
print(items[3][1])


#Values

Libro={
    "Titulo":"100 años de soledad",
    "Autor":"Gabriel garcia marquez",
    "Año de publicacion":1967,
}

valores = list(Libro.values())

print(valores[1]), #Solo imprimer el valor de categoria



#Get (clave,valor_por_defecto)

Estudiante={
    "nombre":"Noah beleño",
    "edad": 20,
    "carrera":"sistema",
}

nombre=Estudiante.get("nombre","No disponible")
print(nombre)
edad=Estudiante.get("edad","No disponible")
print(edad)
correo=Estudiante.get("correo","No disponible")
print(correo)



#Ahora con ciclos for

persona={
    "nombre":"Noah beleño",
    "edad":15,
    "cuidad":"Barranquilla",
}

for clave in persona.keys():
    print(clave)
    
for valor in persona.values():
    print(valor)
    
for clave,valor in persona.items():
    print(clave,valor)
    
