from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import FormAddAuthor, FormEditAuthor
from .models import Book, Author, BookInstance


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'text_head': 'На нашем сайте вы можете получить книги в электронном виде',
        'books': Book.objects.all(),
        'num_books': Book.objects.all().count(),
        'num_instances': BookInstance.objects.all().count(),
        'num_instances_available': BookInstance.objects.filter(status__exact=2).count(),
        'authors': Author.objects,
        'num_authors': Author.objects.count(),
        'num_visits': num_visits
    }

    return render(request, 'catalog/index.html', context)


def about(request):
    context = {
        'text_head': 'Сведения о компании',
        'name': 'ООО "Интеллектуальные информационные системы"',
        'rab1': 'Разработка приложений на основе систем ИИ',
        'rab2': 'Распознавание объектов дорожной инфраструктуры',
        'rab3': 'Создание графических АРТ-объектов на основе систем ИИ',
        'rab4': 'Создание цифровых интерактивных книг, автоматизированных обучающих систем',
    }

    return render(request, 'catalog/about.html', context)


def contact(request):
    context = {
        'text_head': 'Контакты',
        'name': 'ООО "Интеллектуальные информационные системы"',
        'address': 'Москва, ул. Планерная, д.20, к.1',
        'tel': '495-345-45-45',
        'email': 'iis_info@mail.ru',
    }

    return render(request, 'catalog/contact.html', context)


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'  # noqa
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects\
            .filter(borrower=self.request.user)\
            .filter(status__exact='2')\
            .order_by('due_back')


# Book

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    paginate_by = 3


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = "catalog/books_list.html"
    paginate_by = 3


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books_edit')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books_edit')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books_edit')


def books_edit(request):
    context = {
        'book': Book.objects.all(),
    }

    return render(request, "catalog/books_edit.html", context)


# Author

class AuthorListView(ListView):
    model = Author
    paginate_by = 4


class AuthorDetailView(DetailView):
    model = Author


def authors_edit(request):
    author = Author.objects.all()

    context = {
        'author': author,
    }

    return render(request, "catalog/authors_edit.html", context)


def author_edit(request, author_id):
    author = Author.objects.get(id=author_id)
    # author = get_object_or_404(Author, pk=author_id)

    if request.method == "POST":
        instance = Author.objects.get(pk=author_id)
        form = FormEditAuthor(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/authors_edit/")
    else:
        content = {
            "form": FormEditAuthor(instance=author)
        }

        return render(request, "catalog/author_edit.html", content)


def author_add(request):
    if request.method == 'POST':
        form = FormAddAuthor(request.POST, request.FILES)

        if form.is_valid():
            obj = Author.objects.create(
                first_name=form.cleaned_data.get("first_name"),
                last_name=form.cleaned_data.get("last_name"),
                date_of_birth=form.cleaned_data.get("date_of_birth"),
                about=form.cleaned_data.get("about"),
                photo=form.cleaned_data.get("photo"),
            )
            obj.save()

            return HttpResponseRedirect(
                reverse('authors')
            )
    else:
        context = {
            "form": FormAddAuthor()
        }
        return render(request, "catalog/authors_add.html", context)


def author_delete(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
        author.delete()

        return HttpResponseRedirect("/authors_edit/")

    except (Exception,):
        return HttpResponseNotFound("<h2>Автор не найден</h2>")
