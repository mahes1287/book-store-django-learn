from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = 'List of existing books with order by date_publish field.'

    def add_arguments(self, parser):
        parser.add_argument('sorted', nargs='+', type=str)

    def handle(self, *args, **options):
        if options['sorted'][0] == 'asc':
            books_list = Book.objects.order_by('date_publish')
        elif options['sorted'][0] == 'desc':
            books_list = Book.objects.order_by('-date_publish')
        else:
            self.stdout.write('Specify parametr "sorted" to "asc" or "desc"!')
            return
        for book in books_list:
            book_information = 'Book: {}, Authors: {}, ISBN {}, price: {}, date publish - {}'.format(
                book.book_title,
                book.authors_info,
                book.isbn,
                book.price,
                book.date_publish)
            self.stdout.write(book_information, ending='\r\n')
