from django.db import models

# Create your models here.
class personas(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255, verbose_name="Nombres:")
    apellidos = models.CharField(max_length=255, verbose_name="Apellidos:")
    correo = models.CharField(max_length=255, verbose_name="Correo:")
    foto = models.ImageField(upload_to='imagenes/', null=True, blank=True, verbose_name="Foto:") 
    
    def _str_(self):
        fila = "Nombres: "+ self.nombres + " - " + "Apellidos: "+ self.apellidos + " - " + "Correo: "+ self.correo
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()
        