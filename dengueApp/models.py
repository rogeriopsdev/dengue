from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario =models.AutoField(primary_key=True)

class Local(models.Model):
    id_local  = models.AutoField(primary_key=True)
    foto_local =models.ImageField(blank=False, null=False)
    cod_local =models.CharField(max_length=200, null=True)
    id_usuario =models.ForeignKey(Usuario,models.DO_NOTHING,db_column='id_usuario', blank=True, null=True)
