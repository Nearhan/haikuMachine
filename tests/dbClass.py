from pymongo import Connection


class Mongo(object):

	def __init__(self):

		self.connection = Connection()
		self.db = self.connection.test_db
		self.collection = self.db.words
