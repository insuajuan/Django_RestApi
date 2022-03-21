'''
CREAR PROYECTO Y APPS:

Para empezar un proyecto:
>> django-admin startproject PROJECT_NAME

Para crear una app:
>> python manage.py startapp APP_NAME

Cada vez que creo una app, voy a la carpeta del proyecto, 
y dentro de settings.py agrego el nombre de la app al listado "INSTALLED APPS"

Run server:
python manage.py runserver 8000 (por defecto es 8000 si no declaro el puerto)

/////////////////////////
ADMIN

>> python manage.py createsuperuser

Creo mi usuario y contraseña y me logue en mi puerto/admin/login

Para darle acceso a la vista de los distintos modelos que creemos, 
tenemos que ir a la carpeta de la app, y al archivo admin.py

from django.contrib import admin
from .models import Product

admin.site.register(Product)

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
Por ejemplo manejo el request y en base al query busco el dato en la base de datos

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

//////////////////////////////

SERIALIZERS
Utilizamos la libreria rest_framework

Creamos un archivo "serializers.py" dentro de la app products en este caso. Definimos nuestro modelo

from rest_framework import serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]

En views.py, vamos a utilizar serializer para dar respuesta e interactuar con la DB
is_valid y raise_exception se encargan de validar q se manden campos obligatorios en la req, 
y sino genera la excepcion aclarando.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(req, *args, **kwargs):
    serializer = ProductSerializer(data=req.data)
    # Validate if it matches the serialized Model (in serializers.py)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data) 


/////////////////////////
AUTHENTICATION
https://www.django-rest-framework.org/api-guide/authentication/

Podemos agregar a nuestras clases en views.py lo siguiente, para que haya autenticacion

from rest_framework import permissions, authentication

permission_classes = [permissions.IsAuthenticated]
authentication_classes = [authentication.SessionAuthentication] 

or we can asses the permisions given 
permission_classes = [permissions.DjangoModelPermissions]

/////////////////////////
TOKEN AUTHENTICATION

Tenemos que agregar al listado de "installed Apps" en settings.py del Proyecto: rest_framework.authtoken
Luego hacemos un migrate para que se guarden los cambios
>> python manage.py migrate

If we then log in as the superadmin we will see the menu for handling access tokens

/////////////////////////

REACT IN DJANGO:
guardo la carpeta frontend dentro de la q aloja django, y hago:
>> npm run build

Tengo que ademas agregar en settings.py del Proyecto lo siguiente:

En "Templates" agregar: 'DIRS': [BASE_DIR / 'frontend/build']

Debajo de "Static_Url" agrego una nueva linea que sea: "STATICFILES_DIRS = [BASE_DIR / 'frontend/build/static']



'''