from django.contrib import admin

# Register your models here.

from .models import Wishlist, Gift


class GiftInline(admin.TabularInline):
    model = Gift
    extra = 5


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    inlines = [GiftInline]