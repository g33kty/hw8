import json
from models import Author, Quote

def load_authors(filename='authors.json'):
    with open(filename, 'r', encoding='utf-8') as file:
        authors = json.load(file)
        for author in authors:
            if not Author.objects(fullname=author['fullname']).first():
                Author(
                    fullname=author['fullname'],
                    born_date=author['born_date'],
                    born_location=author['born_location'],
                    description=author['description']
                ).save()

def load_quotes(filename='quotes.json'):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = json.load(file)
        for quote in quotes:
            author = Author.objects(fullname=quote['author']).first()
            if author:
                Quote(
                    tags=quote['tags'],
                    author=author,
                    quote=quote['quote']
                ).save()

if __name__ == '__main__':
    load_authors()
    load_quotes()
    print("Дані успішно завантажено до бази даних!")
