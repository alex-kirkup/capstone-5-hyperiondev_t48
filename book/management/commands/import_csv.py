import pandas as pd
import random

from django.core.management.base import BaseCommand, CommandError

from author.models import Author
from book.models import Book
from publisher.models import Publisher


###################################################
## import amazon data science book list csv
###################################################
def import_amazon_data_science_book_list_csv(csv_dir_path: str):

    #functions
    def get_author_list(row):
        #correct for brackets in csv
        authors = str(row['author'])[1:-1].split(',')
        author_list = []
        for author in authors:
            author = author.strip().title()
            if author:
                if author != "and" and author != "et al.":
                    author_names = author.split(" ")
                    for name in reversed(author_names):
                        name = name.strip()
                        if name.lower() in author_names_to_remove:
                            author_names.remove(name)
                    last_name = author_names[-1]
                    first_name = ""
                    for name in author_names[:-1]:
                        first_name += name + " "
                    first_name = first_name.strip()
                    author = (first_name, last_name)
                    author_list.append(author)
        return author_list

    def get_publisher_str(row):
        return (
            str(row['publisher'])
                .split('(')[0]
                .split(';')[0]
                .strip()
        )

    #read csv
    df = pd.read_csv(csv_dir_path + r"\final_book_dataset_kaggle2.csv", delimiter=",")

    #remove rows with NA for title or author
    drop_na_columns = [
        'title',
        'author',
        'publisher',
    ]
    df = df.dropna(
        subset=drop_na_columns,
    )

    #create author set and publisher set
    author_set = set()
    publisher_set = set()
    author_names_to_remove = [
        'dr',
        'dr.',
        'phd',
        'phd.',
        'ph.d',
    ]
    for index, row in df.dropna(subset='author').iterrows():

        #author
        for author in get_author_list(row):
            author_set.add(author)

        #publisher
        publisher_str = get_publisher_str(row)
        if publisher_str:
            publisher_set.add(publisher_str)


    #insert author list into database
    author_object_list = []
    for author in author_set:
        author_object_list.append(
            Author(
                first_name=author[0],
                last_name=author[1],
            )
        )
    Author.objects.bulk_create(author_object_list)

    #insert publisher list into database
    publisher_object_list = []
    for publisher in publisher_set:
        publisher_object_list.append(
            Publisher(
                name=publisher,
            )
        )
    Publisher.objects.bulk_create(publisher_object_list)

    #insert book with publisher and authors for every row in csv
    for index, row in df.dropna(subset='author').iterrows():
            
        try:
            publisher = Publisher.objects.get(
                name = get_publisher_str(row)
            )
        except:
            publisher = None

        book = Book.objects.create(
            title = row['title'],
            isbn = row['ISBN_13'],
            publisher = publisher,
            quantity = random.randint(0,15),
        )
        for author in get_author_list(row):
            book.authors.add(
                Author.objects.get(
                    first_name=author[0],
                    last_name=author[1],
                )
            )


#
#
#
#
#
###################################################
## run these
###################################################

#import_amazon_data_science_book_list_csv()



#
#
#
#
#
###################################################
## create commands
###################################################

class Command(BaseCommand):
    help = "Loads data into database"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_dir_path",
            nargs="?",
            default=r"C:\Users\akirkup\hyperiondev_t48\csv"
        )

    def handle(self, *args, **options):
        Author.objects.all().delete()
        Book.objects.all().delete()
        Publisher.objects.all().delete()
        import_amazon_data_science_book_list_csv(options["csv_dir_path"])
        self.stdout.write(
            self.style.SUCCESS(f"Successfully imported data")
        )
