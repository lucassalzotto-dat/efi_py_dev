﻿# Snake Blog

Esta aplicación web de blog está desarrollada con Flask y utiliza MySQL como base de datos. La aplicación incluye funciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar) para usuarios, publicaciones, comentarios y categorías.

## Requisitos

Asegúrate de tener instalados los siguientes componentes:

- Docker: [Instrucciones de instalación de Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Instrucciones de instalación de Docker Compose](https://docs.docker.com/compose/install/)

## Configuración

Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables de entorno:

```env
MYSQL_ROOT_PASSWORD=tupassword
MYSQL_DATABASE=tu_database
```

## Instrucciones de Instalación

Ejecuta el siguiente script para instalar las dependencias y configurar la base de datos:

```bash
./setup.sh
```

Este script instalará las dependencias, iniciará el servicio MySQL, esperará brevemente para asegurarse de que MySQL esté en funcionamiento y ejecutará el archivo SQL para crear el esquema de la base de datos.

## Docker

Puedes ejecutar la aplicación dentro de un contenedor Docker. Utiliza el siguiente comando para construir y ejecutar la imagen:

```bash
docker-compose up --build
```

La aplicación estará disponible en [http://127.0.0.1:5000](http://127.0.0.1:5000).

Para detener la ejecución de los contenedores, utiliza:

```bash
docker-compose down
```

## Estructura del Proyecto

```
.
|──────app/
| |────__init__.py
| |────api/
| |────config.py
| |────dao/
| |────model/
| |────util/
| |────views/
| |────static/
| |────templates/
|──────database_schema.sql
|──────Dockerfile
|──────docker-compose.yml
|──────requirements.txt
|──────setup.sh
|──────.env
|──────main.py
```

## Ejecutar en Desarrollo

Para ejecutar la aplicación en desarrollo, utiliza el siguiente comando:

```bash
python main.py
```

La aplicación estará disponible en [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Unittest

Para ejecutar pruebas unitarias, utiliza el siguiente comando:

```bash
nosetests app/ --with-cov --cover-html --cover-package=app
```

## Referencias

- [Flask](http://flask.pocoo.org/)
- [Flask Extension](http://flask.pocoo.org/extensions/)
- [Flask restplus](http://flask-restplus.readthedocs.io/en/stable/)
- [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
```

