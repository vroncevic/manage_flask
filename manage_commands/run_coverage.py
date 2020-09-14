# -*- coding: utf-8 -*-

"""
 Module
     run_coverage.py
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
     Define class RunCoverage with attribute(s) and method(s).
     Create coverage reports.
"""

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import sys
from os.path import dirname, abspath, join

try:
    import unittest
    from flask_script import Command
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################


class RunCoverage(Command):
    """
        Define class RunCoverage with attribute(s) and method(s).
        Create coverage reports.
        It defines:

            :attributes:
                | cov - Coverage integration object
            :methods:
                | __init__ - Initial constructor
                | run - Create coverage reports
    """

    def __init__(self, cov):
        """
            Initial constructor.

            :param cov: Coverage integration object
            :type: Coverage
            :exceptions: None
        """
        super(RunCoverage, self).__init__()
        self.cov = cov

    def run(self):
        """
            Create coverage reports.

            :return: 0 - success else 1
            :rtype: <int>
            :exceptions: None
        """
        tests = unittest.TestLoader().discover("app_server/tests")
        result = unittest.TextTestRunner(verbosity=2).run(tests)
        if result.wasSuccessful():
            self.cov.stop()
            self.cov.save()
            print("Coverage Summary:")
            self.cov.report()
            basedir = abspath(dirname(__file__))
            coverage_dir = join(basedir, "tmp/coverage")
            self.cov.html_report(directory=coverage_dir)
            print("HTML version: file://{0}/index.html".format(coverage_dir))
            self.cov.erase()
            return 0
        return 1
