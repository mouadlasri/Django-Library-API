from django.views.generic import ListView

from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

    # ListView returns "object_list" through  the template 