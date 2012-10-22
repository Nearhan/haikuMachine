#use this for our forms 
from django.forms import ModelForm
from simpleApp.models import Word


class WordForm(ModelForm):

	class Meta:
		model = Word
		


