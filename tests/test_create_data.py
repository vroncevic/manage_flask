#!/usr/bin/env python

'''
 Module
     test_create_data.py
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
     Defined class CreateDataTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of CreateData.
 Execute
     python3 -m unittest -v test_create_data
'''

import sys
import unittest

try:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from manage_commands.create_data import CreateData
except ImportError as ats_error:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/manage_flask/blob/dev/LICENSE'
__version__ = '1.4.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


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


class CreateDataTestCase(unittest.TestCase):
    '''
        Defined class CreateDataTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of CreateData.
        It defines:

            :attributes:
                | create_data - DB create object.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_create_data_check - test create db data check.
    '''

    def setUp(self):
        '''Call before test cases.'''
        self.app = Flask(__name__)
        self.app.config.from_object(TestConfig)
        self.db = SQLAlchemy(self.app)
        self.create_data = CreateData(self.db)

    def tearDown(self):
        '''Call after test cases.'''
        self.create_data = None

    def test_create_data_check(self):
        '''Test create db data check.'''
        self.assertEqual(self.create_data is not None, True)
        self.create_data.run()


if __name__ == '__main__':
    unittest.main()
