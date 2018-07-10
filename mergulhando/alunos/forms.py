from django import forms as forms
lideres = (
		('Jorge', 'Jorge'),
		('Eloi', 'Eloi'),
		('Mohamed', 'Mohamed')

	)

class NovoAluno(forms.Form):
	nome = forms.CharField(required=True)
	telefone = forms.CharField(max_length=15, required=True)
	celula =  forms.CharField(max_length=40, required=True)
	email = forms.EmailField(required=True)
	lider = forms.ChoiceField(choices=lideres, 	widget=forms.Select(attrs={'class':'input-field'}),required=True)



