import unittest
from api import Api
from processor import Processor

class ApiTest(unittest.TestCase):


	def setUp(self):
		self.Api = Api(source='hacker_news')

	def test_hacker_news_api(self):
		self.assertEqual(self.Api.url, 'http://api.ihackernews.com/page')


	def test_can_retrive_data(self):
		self.Api.fetch_data()
		self.assertTrue(self.Api.json_response)


	def test_to_pass_data_into_processor(self):
		self.test_can_retrive_data()
		self.Processor = Processor(self.json_response)









if __name__ == '__main__':
	unittest.main()