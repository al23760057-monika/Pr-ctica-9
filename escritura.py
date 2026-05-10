archivo = open("test.txt", "w", encoding = "utf-8" ) #se le pasan parámetros, lleva 3 parámetros: dirección de dónde lo quiero crear, modo de apertura

# "r" = read (lectura)
# "w" = write (escritura) --si existe el archivo lo borra y lo vuelve a crear, si no existe lo crea
# "a" = append (agregar al final del archivo)

#apuntador ..

#archivo se vuelve un objeto de la clase file.
#File es una clase.


archivo.write("Hola Mundo") #escribe en el archivo, se le pasa un string, devuelve el número de caracteres escritos
#para evitar que el archivo se corrampa hay que cerrarlo.

archivo.close() #cierra el archivo, es importante cerrarlo para que no se corrompa, si no se cierra el archivo puede quedar bloqueado y no se podrá acceder a él.

#close es una función de la clase file...por eso no lleva parámetros.

archivo.write("Monica")

# "a" = append (agregar, concatenar.



