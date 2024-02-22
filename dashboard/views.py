from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

from shop.models import Product, ProductImage, Category, Feedback
from accounts.models import User
from orders.models import Order, OrderItem
from .forms import *



def is_manager(user):
    try:
        if not user.is_manager:
            raise Http404
        return True
    except:
        raise Http404


@user_passes_test(is_manager)
@login_required
def products(request):
    products = Product.objects.all()
    context = {'title':'Sản phẩm' ,'products':products}
    return render(request, 'products.html', context)


@user_passes_test(is_manager)
@login_required
def categories(request):
    categories = Category.objects.all()
    context = {'title':'Nhãn hàng' ,'categories':categories}
    return render(request, 'categories.html', context)


@user_passes_test(is_manager)
@login_required
def feedback(request):
    feedbacks = Feedback.objects.all()
    context = {'title':'Góp ý' ,'feedbacks':feedbacks}
    return render(request, 'feedback.html', context)


@user_passes_test(is_manager)
@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        files = request.FILES.getlist("upload_images")
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            for i in files:
                ProductImage.objects.create(product=f, image=i)
            messages.success(request, 'Sản phẩm đã được thêm vào')
            return redirect('dashboard:add_product')
    else:
        form = AddProductForm()
    context = {'title':'Thêm sản phẩm', 'form':form}
    return render(request, 'add_product.html', context)


@user_passes_test(is_manager)
@login_required
def delete_product(request, id):
    product = Product.objects.filter(id=id).delete()
    messages.success(request, 'Sản phẩm đã bị xóa', 'success')
    return redirect('dashboard:products')


@user_passes_test(is_manager)
@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sản phẩm đã được cập nhật', 'success')
            return redirect('dashboard:products')
    else:
        form = EditProductForm(instance=product)
    context = {'title': 'Sửa sản phẩm', 'form':form}
    return render(request, 'edit_product.html', context)


@user_passes_test(is_manager)
@login_required
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            print('kkkkk')
            form.save()
            messages.success(request, 'Nhãn hàng đã được thêm vào')
            return redirect('dashboard:add_category')
        else:
            context = {'title':'Thêm nhãn hàng', 'form':form}
            return render(request, 'add_category.html', context)
    else:
        form = AddCategoryForm()
    context = {'title':'Thêm nhãn hàng', 'form':form}
    return render(request, 'add_category.html', context)


@user_passes_test(is_manager)
@login_required
def delete_category(request, id):
    category = Category.objects.filter(id=id).delete()
    messages.success(request, 'Nhãn hàng đã bị xóa', 'success')
    return redirect('dashboard:category')


@user_passes_test(is_manager)
@login_required
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = EditCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nhãn hàng đã được cập nhật', 'success')
            return redirect('dashboard:category')
    else:
        form = EditCategoryForm(instance=category)
    context = {'title': 'Sửa nhãn hàng', 'form':form}
    return render(request, 'edit_category.html', context)


@user_passes_test(is_manager)
@login_required
def orders(request):
    orders = Order.objects.all()
    context = {'title':'Đơn hàng', 'orders':orders}
    return render(request, 'orders.html', context)


@user_passes_test(is_manager)
@login_required
def order_detail(request, id):
    order = Order.objects.filter(id=id).first()
    items = OrderItem.objects.filter(order=order).all()
    context = {'title':'Chi tiết đơn hàng', 'items':items, 'order':order}
    return render(request, 'order_detail.html', context)


@user_passes_test(is_manager)
@login_required
def delete_order(request, id):
    order = Order.objects.filter(id=id).delete()
    messages.success(request, 'Đơn hàng đã bị xóa', 'success')
    return redirect('dashboard:orders')


@user_passes_test(is_manager)
@login_required
def delete_feedback(request, id):
    feedback = Feedback.objects.filter(id=id).delete()
    messages.success(request, 'Feedback đã bị xóa', 'success')
    return redirect('dashboard:feedback')


@user_passes_test(is_manager)
@login_required
def feedback_detail(request, id):
    feedback = Feedback.objects.filter(id=id).all()
    context = {'title':'Thông tin chi tiết Feedback', 'feedback':feedback}
    return render(request, 'feedback_detail.html', context)