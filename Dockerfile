# Utiliza una imagen base más liviana de Python
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia solo los archivos necesarios para instalar las dependencias
COPY requirements.txt /app/

# Instala Gunicorn y las dependencias de Python
RUN pip install --no-cache-dir gunicorn && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos al directorio de trabajo del contenedor
COPY . /app

# Exponer el puerto en el que se ejecutará tu aplicación (ajusta según sea necesario)
EXPOSE 5000

# Iniciar tu aplicación Flask (utiliza main.py como punto de entrada)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
