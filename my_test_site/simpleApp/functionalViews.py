from django.http import HttpResponse
from django.template import RequestContext, loader
from simpleApp.forms import WordForm
from simpleApp.models import Word

def my_word_view(request):
    #functional way to pass the objects around
    if request.method == 'GET':
        t = loader.get_template('word.html')
        form = WordForm()
        words = Word.objects.all()
        context = {'form' : form, 'words' : words}
        c = RequestContext(request, context)
        return HttpResponse(t.render(c))


    # checking request type
    if request.method == 'POST':
        word = request.POST['word']
        syllables = request.POST['syllables']
        text = ' <p> This is the word : {0}, This is the number of syllables {1} </p>'.format(word, syllables)


        ## insert into database
        new_word = Word(word=word, syllables=syllables)
        new_word.save()


        return HttpResponse(text)

