Manage Flask
-------------

**manage_flask** is toolset for configuration setup of Flask App.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|manage_flask python checker| |manage_flask package checker|

|manage_flask github issues| |manage_flask github contributors|

|manage_flask documentation status|

.. |manage_flask python checker| image:: https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_python_checker.yml

.. |manage_flask package checker| image:: https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_package.yml

.. |manage_flask github issues| image:: https://img.shields.io/github/issues/vroncevic/manage_flask.svg
   :target: https://github.com/vroncevic/manage_flask/issues

.. |manage_flask github contributors| image:: https://img.shields.io/github/contributors/vroncevic/manage_flask.svg
   :target: https://github.com/vroncevic/manage_flask/graphs/contributors

.. |manage_flask documentation Status| image:: https://readthedocs.org/projects/manage_flask/badge/?version=latest
   :target: https://manage_flask.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/manage_flask/releases

To install **manage_flask** type the following

.. code-block:: bash

    tar xvzf manage_flask-x.y.z.tar.gz
    cd manage_flask-x.y.z/
    pip install -r requirements.txt
    mv manage.py /FlaskApp/
    mv /manage_commands/ /FlaskApp/

You can use Docker to create image/container.

Dependencies
-------------

**manage_flask** requires next modules and libraries

* `Flask-Migrate - SQLAlchemy database migrations for Flask applications using Alembic <https://pypi.org/project/Flask-Migrate/>`_
* `Flask-Script - Scripting support for Flask <https://pypi.org/project/Flask-Script/>`_

Package structure
------------------

**manage_flask** is based on OOP.

Code structure

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

Copyright (C) 2017 - 2024 by `vroncevic.github.io/manage_flask <https://vroncevic.github.io/manage_flask>`_

**manage_flask** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/manage_flask/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
