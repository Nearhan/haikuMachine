import unittest, json, re
from processor import Processor	

class ProcessorTests(unittest.TestCase):

	def setUp(self):
		self.test_data = json.load(open('json_test_data.txt', 'r'))
		self.processor = Processor(data=self.test_data)

	def test_to_see_if_object_exsist(self):
		self.assertTrue(self.processor)

	def test_raw_data_exsist(self):
		self.assertTrue(self.processor.raw_data)

	def test_selection_or_raw_words(self):

		self.processor.retrive_words()
		self.assertGreater(len(self.processor.raw_words), 0)
		print self.processor.raw_words

	def test_only_valid_words_are_in_data(self):
		self.processor.retrive_words()
		self.processor.clean_words()
		pattern = '^[0-9]|:|?|\\|.$'
		self.NotRegexMatches(self.processor.cleaned_words, )

		


if __name__ == '__main__':
	unittest.main()