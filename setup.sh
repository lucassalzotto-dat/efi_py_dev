# Definir variables de entorno relacionadas con la base de datos
export DATABASE_URI="mysql+pymysql://BD2021:BD2021itec@143.198.156.171:3306/blog_salzotto"
export SECRET_KEY="dev"

# Instalar los paquetes necesarios
pip install -r requirements.txt

# Iniciar el servicio de MySQL 
service mysql start

# Esperar un breve momento para asegurarte de que MySQL esté en funcionamiento
sleep 10

# Ejecutar el archivo SQL para crear el esquema de la base de datos
mysql -u root -pBD2021itec blog_salzotto < /efi_python/database_schema.sql

# Iniciar la aplicación Flask
python main.py
