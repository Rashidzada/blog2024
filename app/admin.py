from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Author, BolgPost,Contact
from .resources import AuthorResource, BolgPostResource

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource

@admin.register(BolgPost)
class BolgPostAdmin(ImportExportModelAdmin):
    resource_class = BolgPostResource



@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('name','email','subject','message')

