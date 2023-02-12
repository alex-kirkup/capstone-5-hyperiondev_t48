from django.db import models

from isbn_field import ISBNField

# Create your models here.

class Book(models.Model):

    class Meta:
        ordering = [
            'title',
        ]

    title = models.CharField(
        verbose_name="Title",
        max_length=200,
    )
    authors = models.ManyToManyField(
        "author.Author",
        verbose_name="Author",
        related_name="Books",
    )
    isbn = ISBNField(
        clean_isbn=False,
    )
    publisher = models.ForeignKey(
        "publisher.Publisher",
        verbose_name="Publisher",
        on_delete=models.DO_NOTHING,
        related_name="Books",
        null=True,
    )
    date_published = models.DateField(
        verbose_name="Date Published",
        null=True,
    )
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
        null=True,
    )
    image = models.ImageField(
        verbose_name="Image",
        null=True,
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Quantity",
        default=0,
    )
    
    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"Book: {self.title}"
    
    @property
    def get_authors_str(self) -> str:
        authors_str = ""
        for author in self.authors.all():
            if authors_str: authors_str += ", "
            authors_str += author.__str__()
        return authors_str