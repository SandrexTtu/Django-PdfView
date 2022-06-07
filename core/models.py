from django.db import models

class Pdf(models.Model):
    დასახელება = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='Pdf')

    def __str__(self):
        return self.დასახელება

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
