from django.urls import path
from marketplace import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    #produk
    path('produk/', views.produk_list, name='produk_list'),
    path('produk/tambah/', views.tambah_produk, name='tambah_produk'),
    path('produk/edit/<int:pk>/', views.edit_produk, name='edit_produk'),
    path('produk/hapus/<int:pk>/', views.hapus_produk, name='hapus_produk'),

    #cart
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/', views.update_cart_quantity, name='cart_update_quantity'),
]
