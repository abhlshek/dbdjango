from django.contrib import admin
from .models import BookModel,StudentId,coll,Bookshop,Reader,Showroom,Union

# Register your models here.

admin.site.register(BookModel)
admin.site.register(StudentId)
admin.site.register(coll)
admin.site.register(Bookshop)
admin.site.register(Reader)
admin.site.register(Showroom)
admin.site.register(Union)