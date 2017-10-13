# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.http import HttpResponse
from .models import Book
from .models import Author
from django.shortcuts import render


# Create your views here.
def index(request):  #this method defined by lida
    all_books = Book.objects.all()
    return render(request, 'book/index1.html', {'all_books': all_books})
    #return render(request, 'book/index2.html', context)


def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'book/detail.html', {'book': book})
