from django import forms
from django.forms import inlineformset_factory
from .models import Wishlist, Gift


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ["name"]


GiftFormSet = inlineformset_factory(
    Wishlist,
    Gift,
    fields=["name", "price", "link"],
    extra=4,
    min_num=1,
    validate_min=True,
    max_num=5,
    validate_max=True,
    can_delete=False,
)