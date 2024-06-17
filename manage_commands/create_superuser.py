# -*- coding: utf-8 -*-

'''
Module
    create_superuser.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class CreateSuperUser with attribute(s) and method(s).
    Creates superuser and insert to database.
'''

import sys
from typing import List

try:
    # During integration uncomment import line
    # from getpass import getpass
    from flask_script.commands import Command  # type: ignore
    from flask_sqlalchemy import SQLAlchemy
    # During integration uncomment import line
    # from app_server.models.model_user import User
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, Free software to use and distributed it.'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/manage_flask/blob/dev/LICENSE'
__version__ = '1.6.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CreateSuperUser(Command):
    '''
        Defines class CreateSuperUser with attribute(s) and method(s).
        Creates superuser and insert to database.

        It Definess:

            :attributes:
                | _db - SQLAlchemy integration object.
            :methods:
                | __init__ - Initials CreateSuperUser constructor.
                | run - create superuser and insert to database.
    '''

    def __init__(self, db: SQLAlchemy) -> None:
        '''
            Initials CreateSuperUser constructor.

            :param db: SQLAlchemy integration object
            :type: <SQLAlchemy>
            :exceptions: None
        '''
        super(CreateSuperUser, self).__init__()  # type: ignore
        self._db: SQLAlchemy = db

    def run(self) -> int:
        '''
            Creates superuser and insert to database.

            :return: 0.
            :rtype: <int>
            :exceptions: None
        '''
        print('Creating superuser account')
        # During integration uncomment lines
        # username, superuser_email = None, None
        # try:
        #     username = raw_input('Insert username of superuser: ')
        #     superuser_email = raw_input('Insert email of superuser: ')
        # except NameError:
        #     username = input('Insert username of superuser: ')
        #     superuser_email = input('Insert email of superuser: ')
        # superuser_password = getpass('Insert password of superuser: ')
        #
        # admin = User(
        #    username=username, password=superuser_password, admin=True
        # )
        # admin.fullname='Flask Superuser'
        # admin.email=superuser_email
        # self._db.session.add(admin)
        # self._db.session.commit()
        print('Done')
        return 0
