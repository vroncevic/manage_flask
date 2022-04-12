<img align="right" src="https://raw.githubusercontent.com/vroncevic/manage_flask/dev/docs/manage_flask_logo.png" width="25%">

# Flask Manage Mechanism

☯️ **manage_flask** is toolset for managing Flask App.

Developed in 🐍 **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![manage_flask python package](https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_package.yml/badge.svg?branch=master)](https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/manage_flask.svg)](https://github.com/vroncevic/manage_flask/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/manage_flask.svg)](https://github.com/vroncevic/manage_flask/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Package structure](#package-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Navigate to **[release page](https://github.com/vroncevic/manage_flask/releases)** download and extract release archive 📦.

To install modules type the following

```bash
tar xvzf manage_flask-x.y.z.tar.gz
cd manage_flask-x.y.z/
pip install -r requirements.txt
mv manage.py /FlaskApp/
mv /manage_commands/ /FlaskApp/
```

During integration please check comments !

You can use docker to create image/container 🚢.

[![manage_flask docker checker](https://github.com/vroncevic/manage_flask/workflows/manage_flask%20docker%20checker/badge.svg)](https://github.com/vroncevic/manage_flask/actions?query=workflow%3A%22manage_flask+docker+checker%22)

### Dependencies

**manage_flask** requires other modules and libraries (Python 2.x/3.x)

```bash
Flask-Migrate      == 2.6.0
Flask-Script       == 2.0.6
```

### Package structure

🧰 Expected manage structure

```bash
├── manage.py
manage_commands/
├── create_database.py
├── create_data.py
├── create_superuser.py
├── drop_database.py
└──  __init__.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/manage_flask/badge/?version=latest)](https://manage_flask.readthedocs.io/projects/manage_flask/en/latest/?badge=latest)

📗 More documentation and info at

- [manage_flask.readthedocs.io](https://manage_flask.readthedocs.io/en/latest/)
- [www.python.org](https://www.python.org/)

### Contributing

[Contributing to manage_flask](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/manage_flask](https://vroncevic.github.io/manage_flask/)

**manage_flask** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/manage_flask/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
