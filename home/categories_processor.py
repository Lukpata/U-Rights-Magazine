from .models import Category


def categories_data(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return context