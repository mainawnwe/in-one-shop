from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category


def product_list(request):
    products = Product.objects.filter(is_active=True).select_related('category')
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'products/list.html', {
        'products': products,
        'categories': Category.objects.all(),
        'current_category': category_slug,
    })


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.select_related('category').prefetch_related('reviews__user'),
        slug=slug,
        is_active=True
    )

    user_review = None
    if request.user.is_authenticated:
        user_review = product.reviews.filter(user=request.user).first()

    distribution = {i: 0 for i in range(1, 6)}
    for review in product.reviews.all():
        distribution[review.score] += 1

    return render(request, 'products/detail.html', {
        'product': product,
        'user_review': user_review,
        'distribution': distribution,
        'reviews': product.reviews.select_related('user')[:20],
    })