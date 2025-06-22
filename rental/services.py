from datetime import date


def return_book(book, rental):
    """Отметка о возвращении книги"""

    if not rental.is_returned:
        rental.is_returned = True
        rental.return_date=date.today()
        if book.count > book.quantity:
            book.quantity +=1
            book.is_available = True
            book.save()
            rental.save()
        else:
            raise ValueError(f"Все книги возвращены!")
    else:
        raise ValueError(f"Книга {book.title} возвращена!")
    return book, rental
