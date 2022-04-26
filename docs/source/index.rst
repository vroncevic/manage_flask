Manage Flask
-------------

☯️ **manage_flask** is toolset for configuration setup of Flask App.

Developed in 🐍 `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|python package| |github issues| |documentation status| |github contributors|

.. |python package| image:: https://github.com/vroncevic/manage_flask/workflows/python%20package/badge.svg
   :target: https://github.com/vroncevic/manage_flask/workflows/python%20package/badge.svg?branch=master

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/manage_flask.svg
   :target: https://github.com/vroncevic/manage_flask/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/manage_flask.svg
   :target: https://github.com/vroncevic/manage_flask/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/manage_flask/badge/?version=latest
   :target: https://manage_flask.readthedocs.io/projects/manage_flask/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

Navigate to release `page`_ download and extract release archive 📦.

.. _page: https://github.com/vroncevic/manage_flask/releases

To install **manage_flask** 📦 type the following

.. code-block:: bash

    tar xvzf manage_flask-x.y.z.tar.gz
    cd manage_flask-x.y.z/
    pip install -r requirements.txt
    mv manage.py /FlaskApp/
    mv /manage_commands/ /FlaskApp/

You can use Docker to create image/container 🚢.

|github docker checker|

.. |github docker checker| image:: https://github.com/vroncevic/manage_flask/workflows/manage_flask%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/manage_flask/actions?query=workflow%3A%22manage_flask+docker+checker%22

Dependencies
-------------

**manage_flask** requires next modules and libraries

* `Flask-Migrate - SQLAlchemy database migrations for Flask applications using Alembic <https://pypi.org/project/Flask-Migrate/>`_
* `Flask-Script - Scripting support for Flask <https://pypi.org/project/Flask-Script/>`_

Package structure
------------------

**manage_flask** is based on OOP.

🧰 Code structure

.. code-block:: bash

    ├── manage.py
    manage_commands/
    ├── create_database.py
    ├── create_data.py
    ├── create_superuser.py
    ├── drop_database.py
    └──  __init__.py

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 by `vroncevic.github.io/manage_flask <https://vroncevic.github.io/manage_flask>`_

**manage_flask** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

🌎 🌍 🌏 Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/manage_flask/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
