from django.db import models

# Create your models here.


class Word(models.Model):
	'''Basic Word Model'''


	word = models.CharField(max_length=20)
	syllables = models.IntegerField()

	def __unicode__(self):
		return self.word



