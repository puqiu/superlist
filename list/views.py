from django.shortcuts import render, redirect
from .models import Item


def home_page(request):
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/thelist/')

    items = Item.objects.all()
    return render(request, 'home.html')


def view_list(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/thelist/')
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
