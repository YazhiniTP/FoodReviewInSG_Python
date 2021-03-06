from django.contrib import admin
from .models import Category,Hotel,Review

class ReviewAdmin(admin.ModelAdmin):
    model=Review
    list_display=('hotel','pub_date','user_name','comment','rating')
    list_filter=['pub_date','user_name']
    search_fields=['comment']

admin.site.register(Hotel)
admin.site.register(Review,ReviewAdmin)
# Register your models here.
