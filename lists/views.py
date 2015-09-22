from django.http import HttpResponse
from django.shortcuts import redirect, render, render_to_response
from lists.models import Item, List

def home_page(request):
	komentar = ''
	if Item.objects.count() == 0 :
		komentar = 'yey, waktunya berlibur'
	elif Item.objects.count() < 5:
		komentar = 'sibuk tapi santai'
	else:
		komentar = 'oh tidak'

	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'home.html', {'komentar' : komentar})	

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items' : items})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/the-only-list-in-the-world/')		
