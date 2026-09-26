from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from apps.products.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
@require_POST
def submit_review(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    form = ReviewForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'Invalid review data. Please check and try again.')
        return redirect(product.get_absolute_url())

    review, created = Review.objects.update_or_create(
        product=product,
        user=request.user,
        defaults={
            'score': form.cleaned_data['score'],
            'title': form.cleaned_data['title'],
            'comment': form.cleaned_data['comment'],
        }
    )

    if created:
        messages.success(request, 'Thank you! Your review has been posted.')
    else:
        messages.success(request, 'Your review has been updated.')

    return redirect(product.get_absolute_url())


@login_required
@require_POST
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    product = review.product
    review.delete()
    messages.success(request, 'Review deleted successfully.')
    return redirect(product.get_absolute_url())