# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from mybooks.models import Book


def main_page(request):
    books = Book.objects.all()
    return render(request, 'main.html', {'books': books})
