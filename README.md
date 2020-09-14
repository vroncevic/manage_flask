# Flask Manage Mechanism

**manage_flask** is toolset for managing Flask App.

Developed in [python](https://www.python.org/) code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/manage_flask/workflows/Python%20package/badge.svg?branch=master)
 [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/manage_flask.svg)](https://github.com/vroncevic/manage_flask/issues)
 [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/manage_flask.svg)](https://github.com/vroncevic/manage_flask/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Package structure](#package-structure)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Navigate to **[release page](https://github.com/vroncevic/manage_flask/releases)** download and extract release archive.

To install modules type the following:

```
tar xvzf manage_flask-x.y.z.tar.gz
cd manage_flask-x.y.z/
pip install -r requirements.txt
mv manage.py /FlaskApp/
mv /manage_commands/ /FlaskApp/
```

### Dependencies

**manage_flask** requires other modules and libraries (Python 2.x/3.x):

```
* getpass
* unittest
* Flask-Migrate (1.4.0)
* Flask-Script (2.0.5)
* coverage (3.4.3)
```

### Package structure

Expected manage structure:

```
.
├── manage.py
├── manage_commands/
│   ├── create_database.py
│   ├── create_data.py
│   ├── create_superuser.py
│   ├── drop_database.py
│   ├── __init__.py
│   ├── run_coverage.py
│   └── run_test.py
├── manage.py
```

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/manage_flask](https://vroncevic.github.io/manage_flask/)

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.
