# Create your views here.
from django.views.generic.list import ListView
from simpleApp.models import Word
from simpleApp.forms import WordForm

from django.views.generic.form import FormView

class WordDetailView(ListView):

	model = Word
	template_name = 'word.html'
	context_object_name = 'words'

	def get_context_data(self, **kwargs):
		#adding form

		form = WordForm()
		context = super(WordDetailView, self).get_context_data(**kwargs)
		context['word_list'] = Word.objects.all()
		context['form'] = form
		return context

