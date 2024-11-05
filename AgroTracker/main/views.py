from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'main/home.html')


def search(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query)

    return render(request, 'main/search_results.html', {
        'results': results,
        'query': query
    })