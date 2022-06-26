from pyexpat import model
from django.db import models
from django.contrib.auth.models import User



class Pdf(models.Model):
    # user = models.ForeignKey(User , on_delete=models.CASCADE , default="")
    დასახელება = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='Pdf')

    def __str__(self):
        return self.დასახელება

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
