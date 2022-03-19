'''
CREAR PROYECTO Y APPS:

Para empezar un proyecto:
>> django-admin startproject PROJECT_NAME

Para crear una app:
>> python manage.py startapp APP_NAME

Cada vez que creo una app, voy a la carpeta del proyecto, 
y dentro de settings.py agrego el nombre de la app al listado "INSTALLED APPS"

/////////////////////////
URL PATTERNS
Dentro de la carpeta de la app, creo un archivo "urls.py" y defino las rutas y lo que van a mostrar.
Lo mismo hago dentro de la carpeta del proyecto. Agrego la ruta a la app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]

////////////////////////
VIEWS
Creo funciones para lo que se va a mostrar/responder en la url

///////////////////////
MODELS
Podemos crear clases con los modelos de nuestra DB

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)


Cada vez que modifico algo tengo que migrar:
>> python manage.py makemigrations
>> python manage.py migrate

Podemos interactuar directo y manejar la DB:
>> python manage.py shell

Una vez que se abre la terminal, importamos el modelo de la DB a modificar y creamos u nregistro por ejemplo:
>> from products.models import Product
>> Product.objects.create(title='Hello World', content='this is amazing', price=0.00)






'''