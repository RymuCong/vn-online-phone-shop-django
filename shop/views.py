from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from shop.models import Product, Category, ProductImage, Feedback
from cart.forms import QuantityForm
from .forms import FeedbackForm

from re import sub

def paginat(request, list_objects, num_list):
	p = Paginator(list_objects, num_list)
	page_number = request.GET.get('page')
	try:
		page_obj = p.get_page(page_number)
	except PageNotAnInteger:
		page_obj = p.page(1)
	except EmptyPage:
		page_obj = p.page(p.num_pages)
	return page_obj

def home_page(request):
	products = Product.objects.all()
	feedback_first = Feedback.objects.first()
	lenfb = len(Feedback.objects.all())
	feedbacks = Feedback.objects.all()[lenfb-2:]
	context = {'title':'SuccesS','products': paginat(request ,products, 6), 'feedbacks': feedbacks, 'feedback_first': feedback_first}
	return render(request, 'home_page.html', context)

def contact (request):
    return render(request, 'contact.html')

def about_us (request):
    return render(request, 'about_us.html')

def product (request):
    products = Product.objects.all()
    context = {'title':'Điện thoại', 'products': paginat(request ,products, 12)}
    return render(request, 'product.html', context)

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đã gửi thông tin thành công', 'success')
            return redirect('shop:contact')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})

def product_detail(request, slug):
	form = QuantityForm()
	product = get_object_or_404(Product, slug=slug)
	related_products = Product.objects.filter(category=product.category).all()[:4]
	context = {
		'title':product.title,
		'product':product,
		'form':form,
		'related_images': ProductImage.get_ralated_images_by_product_id(product.id),
		'favorites':'favorites',
		'related_products':related_products
	}
	if login_required == True :
		if request.user.likes.filter(id=product.id).first():
			context['favorites'] = 'remove'
	return render(request, 'product_detail.html', context)


@login_required
def add_to_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.add(product)
	return redirect('shop:favorites')


@login_required
def remove_from_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.remove(product)
	return redirect('shop:favorites')


@login_required
def favorites(request):
	products = request.user.likes.all()
	context = {'title':'Favorites', 'products':products}
	return render(request, 'favorites.html', context)


def search(request):
	query = request.GET.get('q')
	words = sub(r'\s+', ' ', query).strip().split(' ')
	search_query = Q()
	for s in words :
		search_query &= Q(title__icontains=s)
	products = Product.objects.filter(search_query).all()
	context = {'products': paginat(request ,products, 12)}
	return render(request, 'product.html', context)


def filter_by_category(request, slug):
	"""when user clicks on parent category
	we want to show all products in its sub-categories too
	"""
	result = []
	category = Category.objects.filter(slug=slug).first()
	[result.append(product) \
		for product in Product.objects.filter(category=category.id).all()]
	# check if category is parent then get all sub-categories
	if not category.is_sub:
		sub_categories = category.sub_categories.all()
		# get all sub-categories products 
		for category in sub_categories:
			[result.append(product) \
				for product in Product.objects.filter(category=category).all()]
	context = {'title': 'Nhãn hàng: ' + category.title,'products': paginat(request ,result, 12)}
	return render(request, 'product.html', context)

