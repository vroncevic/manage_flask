# -*- coding: utf-8 -*-

'''
Module
    manage.py
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
    Main entry point of tool manage_flask.
'''

import sys
from typing import List

try:
    from flask_migrate import Migrate, MigrateCommand
    from flask_script import Manager
    from manage_commands.create_database import CreateDatabase
    from manage_commands.drop_database import DropDatabase
    from manage_commands.create_data import CreateData
    from manage_commands.create_superuser import CreateSuperUser
    # Integrate manage_flask to Flask App
    # from app_server import app, db
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

# Integrate manage_flask to Flask App
# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
# manager.add_command('create_db', CreateDatabase(db))
# manager.add_command('drop_db', DropDatabase(db))
# manager.add_command('create_data', CreateData(db))
# manager.add_command('createsuperuser', CreateSuperUser(db))

# Commands:
# python manage.py create_db
# python manage.py db init
# python manage.py db migrate
# python manage.py createsuperuser
# python manage.py create_data
# python manage.py runserver

if __name__ == '__main__':
    # Integrate manage_flask to Flask App
    # manager.run()
    print('Done')
