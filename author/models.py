from django.db import models

# Create your models here.

class Author(models.Model):

    class Meta:
        ordering = [
            'last_name',
            'first_name',
        ]

    last_name = models.CharField(
        verbose_name="Last name",
        max_length=20,
    )
    first_name = models.CharField(
        verbose_name="First name",
        max_length=20,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Author: {self.last_name}, {self.first_name}"
    