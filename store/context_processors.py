from .models import Category

def categories(request):
    categories = Category.objects.all()
    for category in categories:
        category.slug = category.name.replace(' ','-')  # Converts spaces to hyphens

    return {'categories': categories}
