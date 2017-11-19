# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.db.models import Count, Avg
from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from carts.forms import CartAddBookForm
from django.contrib import messages
from .models import Author, Book, Review

import math
import json


class AllAuthorsView(generic.TemplateView):
    template_name = 'book_author_list.html'

    def get_context_data(self, **kwargs):
        context = super(AllAuthorsView, self).get_context_data(**kwargs)
        context['a'] = Author.objects.filter(name__startswith="A")
        context['b'] = Author.objects.filter(name__startswith="B")
        context['c'] = Author.objects.filter(name__startswith="C")
        context['d'] = Author.objects.filter(name__startswith="D")
        context['e'] = Author.objects.filter(name__startswith="E")
        context['f'] = Author.objects.filter(name__startswith="F")
        context['g'] = Author.objects.filter(name__startswith="G")
        context['h'] = Author.objects.filter(name__startswith="H")
        context['i'] = Author.objects.filter(name__startswith="I")
        context['j'] = Author.objects.filter(name__startswith="J")
        context['k'] = Author.objects.filter(name__startswith="K")
        context['l'] = Author.objects.filter(name__startswith="L")
        context['m'] = Author.objects.filter(name__startswith="M")
        context['n'] = Author.objects.filter(name__startswith="N")
        context['o'] = Author.objects.filter(name__startswith="O")
        context['p'] = Author.objects.filter(name__startswith="P")
        context['q'] = Author.objects.filter(name__startswith="Q")
        context['r'] = Author.objects.filter(name__startswith="R")
        context['s'] = Author.objects.filter(name__startswith="S")
        context['t'] = Author.objects.filter(name__startswith="T")
        context['u'] = Author.objects.filter(name__startswith="U")
        context['v'] = Author.objects.filter(name__startswith="V")
        context['w'] = Author.objects.filter(name__startswith="W")
        context['x'] = Author.objects.filter(name__startswith="X")
        context['y'] = Author.objects.filter(name__startswith="Y")
        context['z'] = Author.objects.filter(name__startswith="Z")

        return context


def book_list(request):
    all_books = Book.objects.all().order_by("title")
    query = request.GET.get("q")
    if query:
        all_books = all_books.filter(title__icontains=query).distinct() | \
            all_books.filter(authors__name__icontains=query).distinct() | \
            all_books.filter(genre__icontains=query).distinct()

    paginator = Paginator(all_books, 12)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    if query:
        query = query
    else:
        query = "Books"

    index = books.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    context = {
        "search": query,
        "title": "Displaying all Results for: ",
        'page': page,
        'books': books,
        'all_books': all_books,
        'page_range': page_range
    }

    return render(request, 'book_list.html', context)


def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)

        # Add books to the shopping cart
        cart_book_form = CartAddBookForm()

        # reviews
        reviews = book.review_set.all().order_by('-created_at')
        reviews_count = book.review_set.count()

        avg_rating = book.review_set.aggregate(Avg('rating'))['rating__avg']
        rating_count = book.review_set.aggregate(
            Count('rating'))['rating__count']

        if rating_count > 0:
            range_pos = int(math.floor(avg_rating))
            rating_filled = range(range_pos)
            rating_empty = range(5 - range_pos)
        else:
            rating_filled = None
            rating_empty = None

        templ_context = {
            'book': book,
            'cart_book_form': cart_book_form,
            'review_objs': get_review_stats(reviews),
            'reviews_count': reviews_count,
            'rating_filled': rating_filled,
            'rating_empty': rating_empty,
            'avg_rating': avg_rating,
            'rating_count': rating_count
        }

    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'book_detail.html', templ_context)


def author_list(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
        book_list = Book.objects.all().filter(author=author)
        context = {'author': author, 'book_list': book_list}
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    return render(request, 'book_author.html', context)


def book_review(request, book_id):
    if request.is_ajax():
        try:
            if request.method == 'POST':
                user = request.user
                book_id = book_id
                review_data = json.loads(request.body)
                # print book_id, user, review_data
                if not review_data['rating'] and not review_data['comments']:
                    raise Exception("Need rating or comment")
                review = create_review(
                    book_id, 
                    user,
                    review_data['rating'], 
                    review_data['comments'], 
                    review_data['anonymous']
                )
                review.save()
                messages.add_message(request, messages.INFO, 'Your review was saved!')
                return HttpResponse("Saved")
        except Exception as inst:
            return HttpResponseBadRequest(inst)
    return HttpResponse("OK")
    

def create_review(book_id, user, rating, comments, anonymous):
    book = Book.objects.get(pk=book_id)
    incognito = False
    if anonymous:
        incognito = anonymous
    if rating == 0:
        rating = None
    review = Review(book=book, author=user, rating=rating, comments=comments, anonymous=incognito)
    return review

def get_review_stats(reviews):
    aggs = []
    for review in reviews:
        if review.rating == None:
            aggs.append((review, None))
        else:
            aggs.append((review, {
                "filled": range(review.rating),
                "empty": range(5 - review.rating)
            }))
    return aggs
