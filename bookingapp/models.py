from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.TextField(max_length=100)
    check_in=models.DateField(null=True)
    check_out=models.DateField(null=True)

    def __str__(self):
        return self.name