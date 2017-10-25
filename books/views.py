# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.http import HttpResponse
from django.db.models import Count, Avg
import math
import json

from .models import Book
from .models import Author
from carts.forms import CartAddBookForm
from django.shortcuts import render


# Create your views here.
def index(request):  # this method defined by lida
    all_books = Book.objects.all()
    return render(request, 'book/index1.html', {'all_books': all_books})
    # return render(request, 'book/index2.html', context)


def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)

        #Add books to the shopping cart
        cart_book_form = CartAddBookForm()

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
            'cart_book_form' : cart_book_form,
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


def book_review(request, book_id):
    if request.is_ajax():
        if request.method == 'POST':
            user = request.user
            book_id = book_id
            review_data = json.loads(request.body)
            print book_id, user, review_data
    return HttpResponse("OK")

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
