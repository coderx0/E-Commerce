from django.urls import path
from . import views
urlpatterns = [
    path('',views.cart,name='cart'),
    path('addcart/<int:product_id>/',views.add_cart,name='addCart'),
    path('removecart/<int:product_id>/<int:cart_item_id>/',views.remove_cart,name="removeCart"),
    path('removecartItem/<int:product_id>/<int:cart_item_id>/',views.remove_cart_item,name="removeCartItem"),
]