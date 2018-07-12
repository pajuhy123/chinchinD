from django import forms

STATUS_CHOICES =(
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews')
    )

class RadioForm(forms.Form):
    feature = forms.CharField( widget=forms.RadioSelect(choices=STATUS_CHOICES)),
    #name_feature = forms.CharField()
    