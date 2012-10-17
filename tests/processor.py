#processor class that cleans up data it receives
import json, re

class Processor(object):

	def __init__(self, data):
		self.raw_data = data


	def retrive_words(self):
		self.raw_words = []

		for item in self.raw_data['items']:
			words  = item['title'].split()
			for word in words:
				if word not in self.raw_words:
					self.raw_words.append(word)


	def clean_words(self):
		'''Attemps to clean the words '''

		self.cleaned_words = []
		pattern = '^[0-9]|:|?|\\|.$'
		for word in self.raw_words:
			if re.search(pattern, word):
				pass
			else:
				self.cleaned_words.append(word)





		