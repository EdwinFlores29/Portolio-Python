# Portolio-Python
 Portolio-Python, Carga Imagenes con los jobs de admin, tiene templates y uso bootrstrap
Pasos para levantar el proyecto en Windows
# 1
Revisar tu version de python por cmd

python --version
![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/57af7f60-d42e-4778-a8dd-604952f6d8a9)

# 2
Navega hasta Escritorio de tu pc

cd Desktop

mkdir django_project
![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/8309a045-f456-4e42-9168-e2160b6bf39e)

# 3
Crear la variable virtual

accede a tu nuevo directorio

PS C:\Users\Susan Lagos\Desktop\django_project>

luego escribe 

python -m venv venv

venv\Scripts\activate

(venv) PS C:\Users\Susan Lagos\Desktop\django_project>

luego tienes tu variable de entorno activada
![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/8ea5c98d-4863-44da-882b-cffa5d3d6202)

# 4
Instala la version de django

pip install Django==5.0

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/3372aedb-5f0b-4fef-acd3-685f636676f7)

Si lo deseas puedes actualizar la version con este comando

python.exe -m pip install --upgrade pip

Revisa la version de django

django-admin --version

(venv) PS C:\Users\Susan Lagos\Desktop\django_project> django-admin --version

5.0

(venv) PS C:\Users\Susan Lagos\Desktop\django_project>

# 5
Descargar desde el repositorio

git clone https://github.com/EdwinFlores29/Portolio-Python.git

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/1062c8ba-3cf3-40b1-a7e3-de3efccf78d8)

Recuerda debes tener un carpeta con el nombre Portolio-Python

# 6
Accede al directorio

(venv) PS C:\Users\Susan Lagos\Desktop\django_project> cd Portolio-Python

(venv) PS C:\Users\Susan Lagos\Desktop\django_project\Portolio-Python> dir

veras los archivos base del proyecto. 

NOTA: Este proyecto se baso en el acceso de datos en Postgresql
![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/d22c001b-8bfd-494b-9a58-313b6c8dd142)

lineas de archivo settings.py

DATABASES = {

 'default': {
 
        'ENGINE': 'django.db.backends.postgresql',
        
         'NAME': 'db_portfolio',
         
         'USER': 'edwinflores',
         
         'PASSWORD': 'Dariohakuna2#',
         
         'HOST': 'localhost',
         
         'PORT': '5432',
       }
}
  

Pero este proyecto tambien lo puedes correr para la conexion a MySql es lo haremos a continuacion

Recuerda tener instalado MySQL en tu PC, agregar MySQL a variables de entorno en Windows

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/84aeac17-39c9-47a2-b7cc-3870fcc1c4e5)

puedes revisar con mysql --version

Si utlizar XAMPP para proyectos sobre PHP, como dato interesante puedes tener ambos corriendo sin problemas con Windows con los puertos distintos,

para XAMPP puerto 3306 y para MySQL Workbench puerto 3308, si eres usuario de Ubuntu puedes tener apache2 instalado pero si tienes XAMPP tienes que detener el proceso

de apache2, lo harias de la manera siguiente, CTRL + T, abres la terminal -->

sudo systemctl status apache2, tu password y veras el proceso en ejecucion, luego -->

sudo systemctl stop apache2, el proceso detenido, ahora -->

cd /opt/lampp

sudo ./manager-linux-x64.run, y luego levantas todos los procesos, y recuerda tener los puertos XAMPP 3308 y MySQL Workbench 3308 respectivamente.

En windows no es necesario tener MySQL Workbench de modo grafico, con que personalices la instalacion y dejar solo la terminal de MySQL Workbench suficiente y luego solo

accedes al terminal desde las consultas para SQL

Comandos basicos: 

SHOW DATABASES;

CREATE DATABASE db_portfolio;

USE db_portfolio;

DROP DATABASE db_portfolio;

DROP TABLE users;

DESC users;

SELECT * FROM users;

CREATE TABLE users;

Luego accedes a la terminal MySQL Workbench y creas una base de datos, puedes seguir el tutorial y el nombre para este ejemplo db_portfolio

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/282d90a2-82fc-42ed-8de6-d40f5c1a8bcd)

Ahora cambias el archivo settings.py para la nueva conexion con MySQL Workbench

DATABASES = {

 'default': {
 
        'ENGINE': 'django.db.backends.mysql',
        
         'NAME': 'db_portfolio',
         
         'USER': 'root',
         
         'PASSWORD': 'Dariohakuna2#',
         
         'HOST': 'localhost',
         
         'PORT': '3308',
       }
}

Luego instala la dependencia MySQL Workbench para django

pip install mysqlclient

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/a3d11207-748a-4b57-a402-467066ccf5b5)

actualiza la dependencia pillow para django

python -m pip install Pillow

luego esta dos dependencias -->

python manage.py makemigrations

python manage.py migrate

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/e585f5a3-1945-47f9-8dd1-717013892f96)

luego ejecuta la plantilla de django -->

python manage.py runserver

para ubuntu tendrias que intentar con -->

python3 manage.py runserver e igual para mac

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/1c79970c-f8cf-4ac3-bae0-e87bcb6b4d74)

El proyecto carga unas imagenes con uso de Bootstrap, claro al clonar no hay recursos multimedia, ya que tendremos que subir los comentarios y imagnes de django-admin

puede dar el error al cargar http://127.0.0.1:8000/, intenta con al direccion --> http://127.0.0.1:8000/index/, ya que deje se dejo un ruta mas especifica.

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/1070097c-31fd-493f-9c06-7601e5f248e2)

proyecto vacio, accede a administrador desde, http://127.0.0.1:8000/admin/login/?next=/admin/, pero recuerda no hay usuarios admin, vamos agregar a continuacion -->

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/a3728a89-39c7-4b84-b967-13c099bfedc6)

utilizas este comando, 

python manage.py createsuperuser

agregas nombre de usuario 

email

y la nueva contraseña

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/a21e6ab7-c1be-4c57-8460-fecd072d5c33)

luego vuelves a correr el proyecto

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/8a2b7eb8-da4d-478a-8082-fba1f3ef051b)

agregamos imagen y comments

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/302fbf33-0f3f-4070-bb66-513ffa88726a)

puedes apoyarte con pagina de recursos gratis, https://undraw.co/illustrations

para finalizar, te diriges a http://127.0.0.1:8000/index/, y visualizas los cambios

![image](https://github.com/EdwinFlores29/Portolio-Python/assets/46845817/5e1655da-d386-4adb-94dc-f628a42f72c6)


















