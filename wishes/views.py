from django.shortcuts import render, redirect
from .forms import WishlistForm, GiftFormSet
from .models import Wishlist

def wishlist_form(request):
    if request.method == "POST":
        form = WishlistForm(request.POST)
        formset = GiftFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            wishlist = form.save()
            formset.instance = wishlist
            formset.save()
            return redirect("thanks")
    else:
        form = WishlistForm()
        formset = GiftFormSet()

    return render(request, "wishes/form.html", {"form": form, "formset": formset})


def thanks(request):
    return render(request, "wishes/thanks.html")

def all_wishlists(request):
    wishlists = Wishlist.objects.prefetch_related("gifts").order_by("name")
    return render(request, "wishes/lists.html", {"wishlists": wishlists})