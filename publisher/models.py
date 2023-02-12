from django.db import models

# Create your models here.

class Publisher(models.Model):

    class Meta:
        ordering = [
            'name',
        ]
        
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
    )
    
    def __str__(self):
        return f"Publisher: {self.name}"

    def __repr__(self) -> str:
        return self.__str__()
    