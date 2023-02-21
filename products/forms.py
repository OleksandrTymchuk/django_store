from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    def save(self, commit=True, **kwargs):
        instance = super(ProductForm, self).save(commit=False)
        instance.description = instance.description
        instance.user = kwargs["user"]
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Product
        fields = ["title", "description"]


