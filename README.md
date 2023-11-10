¡SNAKE BLOG!
Este repositorio contiene una aplicación web de Blog desarrollada con Flask que se puede ejecutar en un entorno Dockerizado utilizando Docker y Docker Compose. A continuación, se proporcionan las instrucciones para configurar y ejecutar la aplicación en tu máquina.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

- Docker: [Instrucciones de instalación de Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Instrucciones de instalación de Docker Compose](https://docs.docker.com/compose/install/)

## Instrucciones

1. **Clona el repositorio:**

   ```bash
   git clone <[URL_del_repositorio](https://github.com/lucassalzotto-dat/efi_py_dev.git)>
   cd <efi_py_dev>
   ```

2. **Configura las variables de entorno:**

   Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables de entorno:

   ```env
   DATABASE_URI=mysql+pymysql://<usuario>:<contraseña>@<host>:<puerto>/<nombre_de_base_de_datos>
   SECRET_KEY=<tu_clave_secreta>
   ```

3. **Construye y levanta los contenedores Docker:**

   Utiliza Docker Compose para construir y levantar los contenedores:

   ```bash
   docker-compose up --build
   ```

4. **Accede a la aplicación web:**

   Una vez que los contenedores estén en funcionamiento, puedes acceder a la aplicación web en tu navegador.

5. **Finaliza la ejecución:**

   Para detener la ejecución de los contenedores, simplemente ejecuta:

   ```bash
   docker-compose down
   ```

## Personalización

Si deseas personalizar aún más la aplicación, puedes modificar los archivos dentro del directorio `my_blog`, que contiene el código fuente de tu blog Flask. Asegúrate de volver a construir los contenedores Docker después de realizar cambios en la aplicación.

Esperamos que estas instrucciones te ayuden a configurar y ejecutar tu aplicación Flask utilizando Docker y Docker Compose. Si tienes alguna pregunta o enfrentas problemas, no dudes en contactarnos.

¡Disfruta de tu aplicación Flask con Docker!

 
 
