import random
import string

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'generator/index.html')


def password(request):
    length = int(request.GET.get('length'))

    possible_chars = list()
    if request.GET.get('include_symbols'):
        possible_chars.extend(string.punctuation)
    if request.GET.get('include_upper'):
        possible_chars.extend(string.ascii_uppercase)
    if request.GET.get('include_lower'):
        possible_chars.extend(string.ascii_lowercase)
    if request.GET.get('include_nums'):
        possible_chars.extend(string.digits)

    if not possible_chars:
        return HttpResponse("<h1> Password could not be generated. Please select at least one checkbox before "
                            "submitting")

    random_chars = random.choices(possible_chars, k=length)
    password = ''.join(random_chars)

    return render(request, 'generator/password.html', {'password': password})
