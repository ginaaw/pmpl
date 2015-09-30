from django.http import HttpResponse
from django.shortcuts import redirect, render, render_to_response
from lists.models import Item, List

def home_page(request):
	komentar = 'yey, waktunya berlibur'
	
	return render(request, 'home.html', {'komentar' : komentar})	

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def view_list(request, list_id):
	komentar = ''
	list_ = List.objects.get(id=list_id)
	items = Item.objects.filter(list=list_)
	if Item.objects.filter(list_id=list_id).count() == 0 :
		komentar= 'yey, waktunya berlibur'	
	elif Item.objects.count() < 5:
		komentar = 'sibuk tapi santai'
	else:
		komentar = 'oh tidak'

	return render(request, 'list.html', {'list' : list_, 'komentar' : komentar})

