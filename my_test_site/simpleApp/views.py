# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import ProcessFormView
from simpleApp.models import Word
from simpleApp.forms import WordForm


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

    def post(self, request, *args, **kwargs ):
        '''Manually adding the post function '''

        self.object_list = self.get_queryset()
        word = request.POST['word']
        syllables = request.POST['syllables']

        #create new word and insert into dictionary
        new_word = Word(word=word, syllables=syllables)
        new_word.save()


        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)


class AnotherWordDetailView(ListView, ProcessFormView):

    model = Word
    template_name = 'word.html'
    context_object_name = 'words'



