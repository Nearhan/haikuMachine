import unittest
from api import Api

class ApiTest(unittest.TestCase):

	def test_hacker_news_api(self):

		self.Api(type='hacker_news')
		sefl.assertEqual(self.Api.url, 'http://api.ihackernews.com/page?format=jsonp&callback=yourFunction')


if __name__ == '__main__':
	unittest.main()