archivo = open("test.txt", "a", encoding = "utf-8" ) #se le pasan parámetros, lleva 3 parámetros: dirección de dónde lo quiero crear, modo de apertura


for i in range(50000): 
    archivo.write("Monica\n") #escribe en el archivo, se le pasa un string, devuelve el número de caracteres escritos
    
    archivo.close() #cierra el archivo, es importante cerrarlo para que no se corrompa, si no se cierra el archivo puede quedar bloqueado y no se podrá acceder a él.