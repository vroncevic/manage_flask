# -*- coding: utf-8 -*-

'''
Module
    drop_database.py
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
    Defines class DropDatabase with attribute(s) and method(s).
    Drops database with tables.
'''

import sys
from typing import List

try:
    from flask_script.commands import Command  # type: ignore
    from flask_sqlalchemy import SQLAlchemy
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


class DropDatabase(Command):
    '''
        Defines class DropDatabase with attribute(s) and method(s).
        Drops database with tables.

        It Definess:

            :attributes:
                | _db - SQLAlchemy integration object.
            :methods:
                | __init__ - initial constructor.
                | run - drop database with tables.
    '''

    def __init__(self, db: SQLAlchemy) -> None:
        '''
            Initial constructor.

            :param db: SQLAlchemy integration object
            :type db: <SQLAlchemy>
            :exceptions: None
        '''
        super(DropDatabase, self).__init__()  # type: ignore
        self._db: SQLAlchemy = db

    def run(self) -> int:
        '''
            Drop database with tables.

            :return: 0
            :rtype: <int>
            :exceptions: None
        '''
        print('Dropping database/tables')
        self._db.drop_all()
        print('Done')
        return 0
