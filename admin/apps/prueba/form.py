""" from django import forms


class OfficeForm(forms.ModelForm):
    class Meta: 
        model = Office
        fields = '__all__' """