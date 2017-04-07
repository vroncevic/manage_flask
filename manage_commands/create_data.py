# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask_script import Command

class CreateData(Command):
	"""
	Define class CreateData with attribute(s) and method(s).
	Create initial data and insert to database.
	It defines:
		attribute:
			__db - SQLAlchemy integration object
		method:
			__init__ - Initial constructor
			run - Create initial data and insert to database
	"""

	def __init__(self, db):
		"""
		:param db: SQLAlchemy integration object
		:type: SQLAlchemy
		"""
		super(CreateData, self).__init__()
		self.__db = db

	def run(self):
		print("Not implemented")
		return 0
