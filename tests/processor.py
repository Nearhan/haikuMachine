#processor class that cleans up data it receives
import json

class Processor(object):

	def __init__(self, data):
		self.raw_data = data

		