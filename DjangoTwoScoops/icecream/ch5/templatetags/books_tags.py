# -*- coding: UTF-8 -*-
from django import template
from ch5.models import Book

__author__ = 'ielkin'

register = template.Library()

@register.inclusion_tag("book_snippet.html")
def books_for_author(author):
    books = Book.objects.filter(authors__id=author.id)
    return {'books': books}