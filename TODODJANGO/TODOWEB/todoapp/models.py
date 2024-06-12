from django.db import models


class todomodl(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    aad = models.DateTimeField(auto_now=True)
    imag = models.ImageField( upload_to="saveimage",null= True, blank=True)

