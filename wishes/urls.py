from django.urls import path
from . import views

urlpatterns = [
    path("", views.wishlist_form, name="wishlist_form"),
    path("thanks/", views.thanks, name="thanks"),
    path("lists/", views.all_wishlists, name="all_wishlists"),
]