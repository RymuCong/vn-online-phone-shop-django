from django.urls import path

from shop import views

app_name = "shop"

urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('<slug:slug>', views.product_detail, name='product_detail'),
	path('add/favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
	path('remove/favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
	path('favorites/', views.favorites, name='favorites'),
	path('search/', views.search, name='search'),
	path('filter/<slug:slug>/', views.filter_by_category, name='filter_by_category'),
	path('product/', views.product, name='product'),
	path('contact/', views.contact, name='contact'),
	path('contact/feedback', views.feedback, name='feedback'),
 	path('about-us/', views.about_us, name='about_us'),
]