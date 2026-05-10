import os 
ruta = "test.txt"
size = os.path.getsize(ruta) #devuelve el tamaño del archivo en bytes, se le pasa la ruta del archivo
kb = size / 1024 #convierte el tamaño de bytes a kilobytes
mb = size /(1024**2) #convierte el tamaño de kilobytes a megabytes
print(f"Tamaño: {kb: .2f}")
print(f"Tamaño: {mb: .4f} MB")


