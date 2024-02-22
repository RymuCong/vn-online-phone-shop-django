from django import forms
from django.forms import ModelForm

from shop.models import Product, Category


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
    
class AddProductForm(ModelForm):
    upload_images = MultipleFileField()
    class Meta:
        model = Product
        fields = ['category', 'image','upload_images', 'title','description', 'price','quantity']

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['id'] = 'summernote'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'image','sub_category', 'is_sub']
    

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        self.fields['is_sub'].widget.attrs['class'] = 'form-check-input'
        self.fields['sub_category'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'


class EditProductForm(ModelForm):
    upload_images = MultipleFileField()
    class Meta:
        model = Product
        fields = ['category', 'image','upload_images', 'title','description', 'price','quantity']

    def __init__(self, *args, **kwargs):
        super(EditProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['id'] = 'summernote'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
class EditCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'image','sub_category', 'is_sub']

    def __init__(self, *args, **kwargs):
        super(EditCategoryForm, self).__init__(*args, **kwargs)
        self.fields['is_sub'].widget.attrs['class'] = 'form-check-input'
        self.fields['sub_category'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
            

