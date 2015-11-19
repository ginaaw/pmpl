from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render, render_to_response
from lists.models import Item, List

def home_page(request):
	komentar = 'yey, waktunya berlibur'
	
	return render(request, 'home.html', {'komentar' : komentar})	

def new_list(request):
	list_ = List.objects.create()
	item = Item(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect(list_)

#def add_item(request, list_id):
#	list_ = List.objects.get(id=list_id)
#	Item.objects.create(text=request.POST['item_text'], list=list_)
#	return redirect('/lists/%d/' % (list_.id,))

def view_list(request, list_id):
	komentar = ''
	list_ = List.objects.get(id=list_id)
	error = None
	
	#items = Item.objects.filter(list=list_)
	
	if Item.objects.filter(list_id=list_id).count() == 0 :
		komentar= 'yey, waktunya berlibur'	
	elif Item.objects.filter(list_id=list_id).count() < 5:
		komentar = 'sibuk tapi santai'
	elif Item.objects.filter(list_id=list_id).count() >=5:
		komentar = 'oh tidak'
	
	if request.method == 'POST':
		try:
		#Item.objects.create(text=request.POST['item_text'], list=list_)
			item = Item(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect(list_)
		except ValidationError:
			error = "You can't have an empty list item"
	
	return render(request, 'list.html', {'list' : list_, 'error': error, 'komentar' : komentar})

