from .models import Category

def category_link(request):
    category = Category.objects.all()
    return{'categories': category}