# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from mybooks.forms import BookAddForm
from mybooks.models import Book


def main_page(request):
    books = Book.objects.all()
    return render(request, 'main.html', {'books': books})
def add_book_page(request):
    form = BookAddForm(request.POST or None)
    aded = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            aded = True
    return render(request, 'add_book_page.html', {'form': form, 'eded':aded})
