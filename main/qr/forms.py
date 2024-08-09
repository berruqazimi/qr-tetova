from django import forms
from .models import QRCodeModel

class QRCodeForm(forms.ModelForm):
    class Meta:
        model = QRCodeModel
        fields = ['name','link']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if QRCodeModel.objects.filter(name=name).exists():
            raise forms.ValidationError("QR code model with this Name already exists.")
        return name
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)