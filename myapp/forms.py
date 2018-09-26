from django import forms

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    Contact = forms.IntegerField()
    DOB = forms.DateField(widget = forms.DateInput(attrs={'type':'date'}))
    about = forms.CharField(widget = forms.Textarea())
