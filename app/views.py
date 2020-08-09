from django.shortcuts import render

from .models import Categories, Item

# Create your views here.
def frontend(request):
    """Vue takes care of everything else!"""
    categories = Categories.objects.all()
    items = Item.objects.all()
    
    data = {
        'categories': categories,
        'items': items,
    }
    
    return render(request, 'app/template.html', data)