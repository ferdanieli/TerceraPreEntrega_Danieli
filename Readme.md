Nombre: App educativa de un instituto terciario

Descripción y Uso: la app contiene 3 modelos, los cuales son: 
   Carreras: donde se puede consultar las carreras que ofrece el instituto,
   (nombre de la carrera y número de comisión). 
   ![consulta de la carrera (http://127.0.0.1:8000/app/carreras/)]
   Directores: donde se puede consultar los datos de los directores de carrera
   (nombre, apellido y dirección de correo).
   ![consulta de directores de carrera (http://127.0.0.1:8000/app/directores/)]
   Materias: donde se puede consultar las materias y los puntos de cada una. 
   Estos puntos están, dado que, al averiguar el valor del punto, se puede
   saber el costo de cada materia.
   ![consulta de materias(http://127.0.0.1:8000/app/materias/)]
Aquí mismo se realiza la consulta que se muestra como una lista, y también
está el botón de Buscar para realizar consulta por nombres. 

Además, la app posee 2 botones por cada modelo, uno para Crear (Carreras,
Directores y Materias), y otro para Buscar (Carreras, Directores y Materias).
![crear carrera(http://127.0.0.1:8000/app/carrera/)]
![nuevo director(http://127.0.0.1:8000/app/director/)]
![crear materias(http://127.0.0.1:8000/app/materia/)]
Luego, se puedo observar un mensaje de bienvenida al Instituto, un detalle
respecto al diseño de la app, los textos de estudio y modalidad de cursado
flex.
Al finalizar, se pueden observar 3 testimonios de estudiantes actuales.

Instalación: los requisitos para acceder a la App son los siguientes:

1) Tener una cuenta de GitHub, que puedes crearla en este link ![(https://github.com/)]
2) Instalar git [(https://git-scm.com/download/win)]
3) Instalar pyenv [(https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#git-commands)]
4) Instalar IDE [(https://www.jetbrains.com/pycharm/download/?section=windows)], [(https://www.jetbrains.com/shop/eform/students)]

Una vez realizada la instalación, puedes clonar el proyecto realizando los siguientes pasos:

1) Abrir GitBash y escirbir: cd y nombre de la carpeta en la que deseas guardar el proyecto y das enter.
2) Luego escribes el siguiente comando: git clone https://github.com/ferdanieli/TerceraPreEntrega_Danieli.git y das enter.
3) Ingresar a PyCharm, abrir un proyecto, hacer click derecho en el menú, hacer click en "Open", buscar
la carpeta en donde elegiste clonar el proyecto, buscar y seleccionar el proyecto clonado y hacer click en "OK".
4) De esta manera, se abrirá el proyecto de la App en tu computadora. 
5) Crear el entorno virtual.
6) Tener instalado django, puedes hacerlo con el siguiente comando: pip install django
7) Realizar las migraciones con este comando: python manage.py makemigrations
8) Luego ingresas este comando para aplicar los cambios: python manage.py migrate
9) Crear un usuario inicial utilizando este comando: python manage.py createsuperuser
Aquí debes crear un nombre usuario, una dirección de correo y una contraseña (estos datos pueden no ser reales)
10) Ejecutar el proyecto, en este caso tienes dos opociones:
a) Desde el botón de ejecución del proyecto.
b) Utilizando el siguiente comando: python manage.py runserver
11) Luego, te aparecerá una url en la terminal en la que debes hacer click y, de esa manera,
accederás a la App.
En este link, podrás acceder a un tutorial de youtube en el cual podrás observar de manera dinámica
la aplicación de los pasos detallados anteriormente: [(https://youtu.be/sh4MuVRSHxQ)]
12) Recuerda activar la base de datos. 
