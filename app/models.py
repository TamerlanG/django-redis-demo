from django.db import models

# Create your models here.
class SampleModel(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title