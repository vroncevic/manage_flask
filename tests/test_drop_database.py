#!/usr/bin/env python

'''
 Module
     test_drop_database.py
 Copyright
     Copyright (C) 2022 Vladimir Roncevic <elektron.ronca@gmail.com>
     manage_flask is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     manage_flask is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class DropDatabaseTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of DropDatabase.
 Execute
     python3 -m unittest -v test_drop_database
'''

import sys
import unittest

try:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from manage_commands.drop_database import DropDatabase
except ImportError as ats_error:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################


class BaseConfig(object):
    '''
        Define class BaseConfig with attribute(s) and method(s).
        Base initial configuration class.
        It defines:
            attribute:
                SECRET_KEY - Development key for session accessing
                DEBUG - Enable/Disable debug option
                BCRYPT_LOG_ROUNDS - for bcrypt hashing utilities
                WTF_CSRF_ENABLED - Secure forms
                DEBUG_TB_ENABLED - Flask debug toolbar's
                DEBUG_TB_INTERCEPT_REDIRECTS - Should intercept redirects?
                SQLALCHEMY_TRACK_MODIFICATIONS - Requires extra memory (True)
            method:
                None
    '''

    SECRET_KEY = 'my_precious'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    '''
        Define class TestConfig with attribute(s) and method(s).
        Testing configuration setup.
        It defines:
            attribute:
                SQLALCHEMY_DATABASE_URI - Set DB URI
            method:
                None
    '''

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_phase.sqlite'


class DropDatabaseTestCase(unittest.TestCase):
    '''
        Defined class DropDatabaseTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of DropDatabase.
        It defines:

            :attributes:
                | drop_database - DB drop object.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_drop_database_check - test drop database check.
    '''

    def setUp(self):
        '''Call before test cases.'''
        self.app = Flask(__name__)
        self.app.config.from_object(TestConfig)
        self.db = SQLAlchemy(self.app)
        self.drop_database = DropDatabase(self.db)

    def tearDown(self):
        '''Call after test cases.'''
        self.drop_database = None

    def test_drop_database_check(self):
        '''Test drop database check.'''
        self.assertEqual(self.drop_database is not None, True)
        self.drop_database.run()


if __name__ == '__main__':
    unittest.main()
