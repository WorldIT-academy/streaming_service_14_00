from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(
        max_length = 100,
        required = True,
        widget = forms.TextInput(attrs= {'placeholder': "Ваше ім'я"})
    )
    email = forms.EmailField(
        required = True,
        widget = forms.TextInput(attrs= {"placeholder": "Ваша пошта"})
    )
    message = forms.CharField(
        required= True,
        widget= forms.Textarea(attrs= {"placeholder": "Ваш відгук"})
    )