# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.http import HttpResponse
from django.db.models import Count, Avg
import math

from .models import Book
from .models import Author
from django.shortcuts import render


# Create your views here.
def index(request):  # this method defined by lida
    all_books = Book.objects.all()
    return render(request, 'book/index1.html', {'all_books': all_books})
    # return render(request, 'book/index2.html', context)


def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)

        # reviews
        reviews = book.review_set.all().order_by('-created_at')
        reviews_count = book.review_set.count()

        avg_rating = book.review_set.aggregate(Avg('rating'))['rating__avg']
        rating_count = book.review_set.aggregate(Count('rating'))['rating__count']

        if rating_count > 0:
            range_pos = int(math.floor(avg_rating))
            rating_filled = range(range_pos)
            rating_empty = range(5 - range_pos)
        else:
            rating_filled = None
            rating_empty = None


        templ_context = {
            'book': book,
            'review_objs': get_review_stats(reviews),
            'reviews_count': reviews_count,
            'rating_filled': rating_filled,
            'rating_empty': rating_empty,
            'avg_rating': avg_rating,
            'rating_count': rating_count
        }

    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'book/detail.html', templ_context)


def author_list(request, author_id):

    try:
        author = Author.objects.get(pk=author_id)
        book_list = Book.objects.all().filter(author=author)

        context = {
            'author' : author,
            'book_list': book_list
        }
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    return render(request, 'book/author.html', context )


def get_review_stats(reviews):
    aggs = []
    for review in reviews:
        if review.rating == None:
            aggs.append((
                review,
                None
            ))
        else:
            aggs.append((
                review,
                {
                    "filled": range(review.rating),
                    "empty": range(5 - review.rating)
                }
            ))
    return aggs
