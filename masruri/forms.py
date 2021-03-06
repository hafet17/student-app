from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'custumer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'custumer': 'Konsumen',
            'product': 'Produk',
            'status': 'Status Order',
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        paginate_by = 6
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nama Produk',
            'price': 'Harga Produk',
            'category': 'Kategori Produk',
            'description': 'Deskripsi',
            'tag': 'Tag',
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustumerForm(ModelForm):
    class Meta:
        model = Custumer
        fields = '__all__'
        exclude = ['user']
