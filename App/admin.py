from django.contrib import admin
from .models import Liberian,Book, Book_Allotment,Series,Genre,Publisher,Author,Member,Settings
# Register your models here.
admin.site.register(Liberian)
admin.site.register(Book)
admin.site.register(Book_Allotment)
admin.site.register(Series)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Member)
admin.site.register(Settings)
