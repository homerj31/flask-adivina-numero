# Usamos una imagen base oficial de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de la app al contenedor
COPY app.py /app/

# Instalamos Flask
RUN pip install flask

# Exponemos el puerto 5000
EXPOSE 5000

# Definimos el comando para ejecutar la app
CMD ["python", "app.py"]
