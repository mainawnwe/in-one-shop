from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    score = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in range(5, 0, -1)],
        coerce=int,
        widget=forms.RadioSelect(attrs={'class': 'star-radio'}),
        required=True,
    )

    class Meta:
        model = Review
        fields = ['score', 'title', 'comment']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Review title (optional)'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your experience with this product...'
            }),
        }