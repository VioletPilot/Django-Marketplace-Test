from django.shortcuts import render

from item.models import Category,Item

# Create your views here.
def index(request):
    item= Item.objects.filter(is_sold=False)[0:6]
    category=Category.objects.all()

    return render(request, 'core/index.html',{
        'categories':category,
        'items':item,

    })

def contact(request):
    return render(request, 'core/contact.html')