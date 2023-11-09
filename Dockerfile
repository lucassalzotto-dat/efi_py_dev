# Utiliza una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al directorio de trabajo del contenedor
COPY . /app

# Instala las dependencias de Python desde requirements.txt
RUN pip install -r requirements.txt

# Exponer el puerto en el que se ejecutará tu aplicación (ajusta según sea necesario)
EXPOSE 5000

# Iniciar tu aplicación Flask (utiliza main.py como punto de entrada)
CMD ["python", "main.py"]
