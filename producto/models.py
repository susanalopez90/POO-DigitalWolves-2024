from django.db import models

# Create your models here.
class productos(models.Model):
       
     # Diseñar los campos de mi tabla
    ProductoId = models.AutoField(primary_key=True, auto_created=True)
    Nombre = models.TextField(null=False, max_length=50)
    Descripcion = models.TextField(null=False, max_length=250)
    Precio = models.DecimalField(null=False, decimal_places=2, max_digits=12)
    Cantidad = models.IntegerField(null=False)
    Estado = models.FloatField(null=False)
