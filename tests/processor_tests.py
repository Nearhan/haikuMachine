import unittest, json
from processor import Processor

class ProcessorTests(unittest.TestCase):

	def setUp(self):
		self.test_data = json.load(open('json_test_data.txt', 'r'))
		self.processor = Processor(data=self.test_data)

	def test_to_see_if_object_exsist(self):
		self.assertTrue(self.processor)

	def test_raw_data_exsist(self):
		self.assertTrue(self.processor.raw_data)

		


if __name__ == '__main__':
	unittest.main()