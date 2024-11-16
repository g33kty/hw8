from models import Author, Quote

def search_by_author(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [quote.quote for quote in quotes]
    return []

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [quote.quote for quote in quotes]

def main():
    print("Введіть команду (name: ім'я автора, tag: тег, tags: список тегів, exit для виходу)")
    while True:
        command = input(">>> ")
        if command.startswith("name:"):
            name = command.split(":", 1)[1].strip()
            results = search_by_author(name)
        elif command.startswith("tag:"):
            tag = command.split(":", 1)[1].strip()
            results = search_by_tag(tag)
        elif command.startswith("tags:"):
            tags = command.split(":", 1)[1].strip()
            results = search_by_tags(tags)
        elif command == "exit":
            print("Вихід з програми.")
            break
        else:
            print("Невідома команда!")
            continue

        if results:
            print("\n".join(results))
        else:
            print("Нічого не знайдено.")

if __name__ == '__main__':
    main()
