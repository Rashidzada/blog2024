from import_export import resources
from .models import Author, BolgPost

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class BolgPostResource(resources.ModelResource):
    class Meta:
        model = BolgPost
