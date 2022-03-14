#!/usr/bin/env python

'''
 Module
     test_create_superuser.py
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
     Defined class CreateUserTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of CreateSuperUser.
 Execute
     python3 -m unittest -v test_create_superuser
'''

import sys
import unittest
from unittest.mock import mock_open, patch

try:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from manage_commands.create_superuser import CreateSuperUser
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


class CreateUserTestCase(unittest.TestCase):
    '''
        Defined class CreateUserTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of CreateSuperUser.
        It defines:

            :attributes:
                | daemon_usage - Daemon usage object.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_create_db_user_check - test create db user check.
    '''

    def setUp(self):
        '''Call before test cases.'''
        self.app = Flask(__name__)
        self.app.config.from_object(TestConfig)
        self.db = SQLAlchemy(self.app)
        self.create_db_super_user = CreateSuperUser(self.db)

    def tearDown(self):
        '''Call after test cases.'''
        self.create_db_super_user = None

    @patch(
        'builtins.input',
        side_effect=['vroncevic', 'elektron.ronca@gmail.com', 'admin']
    )
    def test_create_db_user_check(self, mock_input):
        '''Test daemon usage check start.'''
        calling_user = mock_input()
        calling_email = mock_input()
        calling_password = mock_input()
        self.assertTrue(
            self.create_db_super_user is not None and
            calling_user == 'vroncevic' and
            calling_email == 'elektron.ronca@gmail.com' and
            calling_password == 'admin'
        )


if __name__ == '__main__':
    unittest.main()
