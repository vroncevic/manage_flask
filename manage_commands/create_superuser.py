# -*- coding: utf-8 -*-

'''
 Module
     create_superuser.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class CreateSuperUser with attribute(s) and method(s).
     Create superuser and insert to database.
'''

import sys

try:
    from getpass import getpass
    from flask_script import Command
    # TODO During integration uncomment import line
    #from app_server.models.model_user import User
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/manage_flask/blob/dev/LICENSE'
__version__ = '1.5.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CreateSuperUser(Command):
    '''
        Define class CreateSuperUser with attribute(s) and method(s).
        Create superuser and insert to database.
        It defines:

            :attributes:
                | __db - SQLAlchemy integration object.
            :methods:
                | __init__ - initial constructor.
                | run - create superuser and insert to database.
    '''

    def __init__(self, db):
        '''
            Initial constructor.

            :param db: SQLAlchemy integration object.
            :type: <SQLAlchemy>
            :exceptions: None
        '''
        super(CreateSuperUser, self).__init__()
        self.__db = db

    def run(self):
        '''
            Create superuser and insert to database.

            :return: 0.
            :rtype: <int>
            :exceptions: None
        '''
        print('Creating superuser account')
        username, superuser_email = None, None
        try:
            username = raw_input('Insert username of superuser: ')
            superuser_email = raw_input('Insert email of superuser: ')
        except NameError:
            username = input('Insert username of superuser: ')
            superuser_email = input('Insert email of superuser: ')
        superuser_password = getpass('Insert password of superuser: ')
        # TODO During integration uncomment lines for creating admin object
        # admin = User(
        #    username=username, password=superuser_password, admin=True
        # )
        # admin.fullname='Flask Superuser'
        # admin.email=superuser_email
        # self.__db.session.add(admin)
        # self.__db.session.commit()
        print('Done')
        return 0
