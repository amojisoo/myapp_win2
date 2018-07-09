from django import forms

from .models import Info

class Info_Form(forms.ModelForm):

    name = forms.CharField( widget= forms.TextInput(attrs = { "size" : 50} ) )

    class Meta:
        model = Info
        fields = [ "name" , "memo" , "code" ]