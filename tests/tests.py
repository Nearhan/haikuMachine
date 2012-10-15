import unittest 
from dbClass import Mongo


class MongoTest(unittest.TestCase):

	def setUp(self):
		self.Mongo = Mongo()


	def test_check_Mongo_class_init(self):
		self.assertEqual(self.Mongo.connection.HOST, 'localhost')
		self.assertEqual(self.Mongo.db.name, 'test_db')
		self.assertEqual(self.Mongo.collection.name, 'words')

	def test_to_insert_into_collection(self):
		data = { 'word' : 'Danger', 'syallbes' : 2 }
		self.Mongo.collection.insert(data)







if __name__ == '__main__':
	unittest.main()
