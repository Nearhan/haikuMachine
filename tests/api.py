import json, urllib2


class Api(object):

	def __init__(self, source = '', callback = '', type = ''):

		if source == 'hacker_news' and type == 'jsonp':
			self.callback = callback
			self.url = 'http://api.ihackernews.com/page?format=jsonp&callback=' + self.callback

		elif source == 'hacker_news':
			self.url = 'http://api.ihackernews.com/page'

	def fetch_data(self):
		self.json_response = json.load(urllib2.urlopen(self.url))


	def myFunction(self):
		print self.json_response





