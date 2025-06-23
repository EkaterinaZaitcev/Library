from datetime import date

from config.settings import EMAIL_HOST_USER


def return_book(book, rental):
    """Отметка о возвращении книги"""

    if not rental.is_returned:
        rental.is_returned = True
        rental.return_date = date.today()
        if book.count > book.quantity:
            book.quantity += 1
            book.is_available = True
            book.save()
            rental.save()
        else:
            raise ValueError("Все книги возвращены!")
    else:
        raise ValueError(f"Книга {book.title} возвращена!")
    return book, rental


def send_mail(obj):
    """Отправка писем с напоминаниями о возврате книг"""
    subject = "Пора возвращать книгу в библиотеку!"
    message = (f'Уважаемый читатель!'
               f'Срок аренды {obj.book} истекает {obj.return_date}.'
               f'Просим вернуть {obj.book} до указанного срока {obj.return_date}.')
    from_email = EMAIL_HOST_USER
    recipient_list = [obj.user.email]
    send_mail(subject, message, from_email, recipient_list)
