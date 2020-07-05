from django.urls import path,include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = 'home'),
    path('cart',views.cart,name = 'cart'),
    path('home/<int:id>',views.add_to_cart,name = 'add_to_cart'),
    path('cart/<int:id>',views.remove_from_cart,name = 'remove_from_cart'),
    path('quantity_minus/<int:id>',views.quantity_minus,name = 'quantity_minus'),
    path('quantity_plus/<int:id>',views.quantity_plus,name = 'quantity_plus'),
    path('checkout',views.CheckoutView.as_view(), name="checkout"),
    path('payment/<payment_option>',views.PaymentView.as_view(),name = 'payment'),
]   

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)