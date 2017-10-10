# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Book, Author, Category


# Create your views here.
def index(request):  # this method defined by lida
    all_books = Book.objects.all()
    return render(request, 'book/index1.html', {'all_books': all_books})
    # return render(request, 'book/index2.html', context)


def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'book/detail.html', {'book': book})


def book_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
    return render(request, 'book/list.html', {'category': category,
                                              'categories': categories, 'books': books})
