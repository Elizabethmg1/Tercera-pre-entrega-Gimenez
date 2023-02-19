# Tercera-pre-entrega-Gimenez

## Explicacion de funcionalidades:
 En primer lugar se crea el proyecto con django-admin startproject backend,
 
 luego se crea la aplicacion con python manage.py startproject app,
 
 luego se agrega la app en el archivo settings.py
 
 se agregan los modelos en el archivo models.py, en este caso los modelos son "Hermana", "Prima" y "Tia"
 
 luego se suben estos modelos a la base de datos con python manage.py makemigrations, python manage.py sqlmigrate app 0001 y python manage.py migrate
 
 despues de esto las tablas estan creadas en la base de datos sqlite
 
 Se empieza a trabajar sobre las views la cual genera una vista para Hermana, Prima y tia las cuales se relacionan cada una con un template los cuales heredan el html del archivo padre.html
 
 Tambien  se genera vistas para ingresar y buscar datos en la base de datos con formularios para eso se crea el archivo forms.py y estas vistas se relacionan cada una con un template que heredan el html del archivo padreformularios.html
 
 Luego se agregan todas estas vistas al archivo urls.py
 
 Se activa la web con python manage.py runserver
 
 y luego se accede a agregar objetos a la base de datos con las siguientes urls:
 
 - http://127.0.0.1:8000/HermanaFormulario/
 
 - http://127.0.0.1:8000/PrimaFormulario/
 
 - http://127.0.0.1:8000/TiaFormulario/
 
 tambien se pueden buscar datos en la base de datos con los siguientes urls:
 
 - http://127.0.0.1:8000/BusquedaHermana/
 
 - http://127.0.0.1:8000/BusquedaPrima/
 
 - http://127.0.0.1:8000/BusquedaTia/
