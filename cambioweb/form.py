from django import forms

class Form(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super().__init__(*args, **kwargs)

        self.fields['moeda'] = forms.ChoiceField(choices=choices)
        self.fields['valor'] = forms.CharField(label='Valor')
