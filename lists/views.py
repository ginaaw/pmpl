from django.shortcuts import redirect, render
from lists.models import Item

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
		return redirect('/')
		
	items = Item.objects.all()
	return render(request, 'home.html', {'items' : items, 'komentar' : komentar})
		
