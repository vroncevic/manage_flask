# Flask Manage Mechanism (Python 2.x/3.x).

manage_flask is toolset for managing Flask App.

Developed in python code: 100%.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

Part of Flask Web Project.

![Python package](https://github.com/vroncevic/manage_flask/workflows/Python%20package/badge.svg?branch=master)

### INSTALLATION
Navigate to release [page](https://github.com/vroncevic/manage_flask/releases/tag/v1.0) download and extract release archive.

To install this set of modules type the following:

```
tar xvzf manage_flask-1.0.tar.gz
```

### DEPENDENCIES

These modules requires other modules and libraries (Python 2.x/3.x):

```
* getpass
* unittest
* Flask-Migrate-1.4.0
* Flask-Script-2.0.5
* coverage-3.4.3
```

### PACKAGE STRUCTURE

Expected manage structure:

```
.
├── manage_commands
│   ├── create_database.py
│   ├── create_data.py
│   ├── create_superuser.py
│   ├── drop_database.py
│   ├── __init__.py
│   ├── run_coverage.py
│   └── run_test.py
├── manage.py
```

### COPYRIGHT AND LICENCE

Copyright (C) 2017 by https://github.com/vroncevic/manage_flask

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7.9/3.4.2 or,
at your option, any later version of Python 3 you may have available.

:sparkles:
